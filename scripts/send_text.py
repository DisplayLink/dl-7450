# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024

import sys
import argparse
import requests
import base64

API = "https://sandbox.vision.synaptics.com/api"


def ParseArgs():
    parser = argparse.ArgumentParser(
        description="This is a tool to send text message to the running application on a Navarro dock",
        epilog="""Example use:
          send_text -k myKey -s mySecret -e myEnterprise -d myDockId -t <text message> """,
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
        help="The dock ID that the text message will be sent to",
    )
    parser.add_argument(
        "-t",
        "--text",
        required=True,
        help="The text message to send",
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


def send_text(token: str, dock_id: str, text: str) -> requests.Response:
    extra_headers = {"Authorization": f"Bearer {token}"}
    message = bytes("t" + text, encoding="utf-8")
    payload = {"data": {
        "type": "applicationMessage",
        "attributes": {
            "dockId": dock_id,
            "message": base64.b64encode(message).decode("utf-8")
        }
    }
    }
    print("Sending text message...")

    response = requests.post(
        f"{API}/docks/application/message",
        json=payload,
        headers=extra_headers)
    if response.status_code != 201:
        raise ValueError(f"Send Text Message Failed: {response.text}")

    return response


def Main():
    args = ParseArgs()

    token = access_token(args.key, args.secret, args.enterprise)

    # Convert any actual newline characters back to the literal '\n'
    args.text = args.text.replace('\\n', '\n')

    send_text(token, args.dock, args.text)

    print("Text message sent successfully")

    return 0


if __name__ == "__main__":
    sys.exit(Main())
