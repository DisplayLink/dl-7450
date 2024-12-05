# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024

import os
import sys
import argparse
import requests
import base64
import yaml
from pprint import pformat
from typing import Dict, Any
from string import Template


API = "https://sandbox.vision.synaptics.com/api"


def parse_args():
    parser = argparse.ArgumentParser(
        description="This is a tool to send RomStore data a Navarro dock",
        epilog="""Example use:
          send_rom_store -k myKey -s mySecret -e myEnterprise -d myDockId -c <rom_store_config_file> """,
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
        "-c",
        "--config_file",
        required=True,
        help="The config rom store file to be sent",
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


def check_paths(obj, parent_key=""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "path":
                if not os.path.exists(value):
                    raise FileNotFoundError(
                        f"Path '{value}' does not exist (key: {parent_key})")
            else:
                check_paths(value, parent_key=key)
    elif isinstance(obj, list):
        for item in obj:
            check_paths(item)


def parse_config_file(config_file: str) -> Dict[str, Any]:

    # Allowed top-level keys
    ALLOWED_KEYS = {"images", "kv_store", "code"}
    # Load the YAML file
    try:
        with open(config_file, 'r') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {config_file} does not exist.")
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML file: {e}")

    if data is None:
        return {}

    condfig_file_abs_path = os.path.dirname(os.path.abspath(config_file))
    data = eval(
            Template(str(data)).safe_substitute(
                {"CONFIG_PATH": condfig_file_abs_path}
            )
    )

    # Check for the existence of paths
    for key in ALLOWED_KEYS:
        if key in data:
            check_paths(data[key], parent_key=key)

    print("YAML file is valid and all paths exist.")

    return data


def send_rom_store(token: str, dock_id: str, code: bytes, images: dict, kv_store: dict) -> requests.Response:
    extra_headers = {"Authorization": f"Bearer {token}"}
    payload = {"data": {
        "type": "applicationRomStore",
        "attributes": {
            "dockId": dock_id,
            "code": {
                "code": base64.b64encode(code).decode("utf-8"),
            },
            "images": images,
            "kvStore": kv_store
        }
    }
    }
    print("Sending RomStore Message ...")

    response = requests.post(
        f"{API}/docks/application/romstore",
        json=payload,
        headers=extra_headers)
    if response.status_code != 200:
        raise ValueError(
            f"Send RomStore Message Failed:\nresponse.status_code = {response.status_code} \nresponse.text = {response.text}")

    return response


def main():
    args = parse_args()

    token = access_token(args.key, args.secret, args.enterprise)

    rom_store_config = parse_config_file(args.config_file)

    # read code
    code_bytes = b''
    if "code" in rom_store_config:
        code_bytes = open(rom_store_config['code']['path'], "rb").read()

    # read images
    images = {}
    if "images" in rom_store_config:
        images = {
            name: {
                "type": details.get("type").upper(),
                "data": base64.b64encode(open(details.get("path"), "rb").read()).decode("utf-8")
            }
            for name, details in rom_store_config['images'].items()
        }

    # read kv_store
    kv_store = {}
    if "kv_store" in rom_store_config:
        kv_store = {
            key: value
            for key, value in rom_store_config['kv_store'].items()
        }

    send_rom_store(token, args.dock, code_bytes, images, kv_store)

    print("ROM store config sent successfully. Please wait 1 minute for the new ROM store to apply itself to your dock. You may reboot your dock after this.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
