# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024

import sys
import argparse
import requests
import base64

API = "https://sandbox.vision.synaptics.com/api"


def parse_args():
    parser = argparse.ArgumentParser(
        description="This is a tool to send image to the running application on a Navarro dock",
        epilog="""Example use:
          send_image -k myKey -s mySecret -e myEnterprise -d myDockId -f <image file path> """,
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
        help="The dock ID that the image will be sent to",
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="The file path for the image to send",
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


def send_image(token: str, dock_id: str, img: bytes) -> requests.Response:
    extra_headers = {"Authorization": f"Bearer {token}"}
    message = bytes("i", encoding="utf-8") + img
    payload = {"data": {
        "type": "applicationMessage",
        "attributes": {
            "dockId": dock_id,
            "message": base64.b64encode(message).decode("utf-8")
        }
    }
    }
    print("Sending image...")

    response = requests.post(
        f"{API}/docks/application/message",
        json=payload,
        headers=extra_headers)
    if response.status_code != 201:
        raise ValueError(f"Send Image Failed: {response.text}")

    return response


def main():
    args = parse_args()

    token = access_token(args.key, args.secret, args.enterprise)

    with open(args.file, "rb") as img:
        send_image(token, args.dock, img.read())

    print("Image sent successfully")

    return 0


if __name__ == "__main__":
    sys.exit(main())
