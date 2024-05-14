# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024

import sys
import argparse
import requests
import base64

API = "https://sandbox.vision.synaptics.com/api"

def ParseArgs():
    parser = argparse.ArgumentParser(
        description="This is a tool to send python code to a Navarro dock",
        epilog="""Example use:
          send_code -k myKey -s mySecret -e myEnterprise -d myDockId -f file.py """,
    )

    parser.add_argument(
        "-k",
        "--key",
        required=True,
        help="Application Key for Authentication",
    )
    parser.add_argument(
        "-s",
        "--secret",
        required=True,
        help="Application Secret for Authentication",
    )
    parser.add_argument(
        "-e",
        "--enterprise",
        required=True,
        help="Enterprise ID to login to",
    )
    parser.add_argument(
        "-d",
        "--dock",
        required=True,
        help="The dock ID that the message will be sent to",
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="The python application code",
    )

    return parser.parse_args()

def access_token(key: str, secret: str, enterprise: str) -> str:
    application_login = {
        "data": {
            "attributes": {
                "clientId": key,
                "clientSecret": secret,
                "enterpriseId": enterprise,
            },
            "type": "isvApplicationLogin",
        }
    }

    response = requests.post(API + "/isv/application/login", json=application_login)
    if response.status_code != 201:
        raise ValueError(f"Login Unsuccessful: {response}")
    return response.json()["data"]["attributes"]["accessToken"]

def send_code(token: str, dock_id: str, code: bytes) -> requests.Response:
    extra_headers = {"Authorization": f"Bearer {token}"}
    request = {"data": {
        "type": "applicationCode",
        "attributes": {
            "dockId": dock_id,
            "code": base64.b64encode(code).decode("utf-8")
        }
    }}

    response = requests.post(
        f"{API}/docks/application/code",
        json = request,
        headers=extra_headers)

    if response.status_code != 200:
        raise ValueError(f"Send Code Failed: {response.text}")

    return response


def Main():
    args = ParseArgs()

    token = access_token(args.key, args.secret, args.enterprise)

    with open(args.file, "rb") as f:
        code = f.read()

    send_code(token, args.dock, code)

    print("Code sent successfully")

    return 0

if __name__ == "__main__":
    sys.exit(Main())

