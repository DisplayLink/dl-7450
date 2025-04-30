# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024-2025

from datastore import ImageStore, KvStore
from splashscreen import Splashscreen, Alignment
from network import LAN
from wakeup import wakeup

class Application:
    background = "default"
    #background = "screen_2"
    #background = "screen_3"

    layout = {
        "text_box": {
            "x": 960, "y": 850,
            "alignment": Alignment.MIDDLE
        },
        "banner": {
            "x": 960, "y": 80,
            "alignment": Alignment.MIDDLE
        }
    }

    def __init__(self):
        kv_store = KvStore()
        self.dock_name = kv_store.get("dock_name")
        self.screen = Splashscreen()
        self.nic = LAN()
        self.timer = None

    def __del__(self):
        self.timer.cancel()

    def set_background(self):
        image_store = ImageStore()
        image_token = image_store.get_token(self.background)
        self.screen.set_background(image_token)

    def set_banner(self):
        banner = "<span size=\"large\"><b>Welcome to the DisplayLink DL-7450 SDK Workshop</b></span>"
        self.screen.add_text_box(banner, self.layout["banner"])

    def display_text(self):
        ip, _, _, _ = self.nic.ifconfig()
        text = [ f"Dock: {self.dock_name}" ]
        if len(ip) == 0:
            text.append("Waiting for network...")
        else:
            text.append(f"IP Address: {ip}")
            self.timer.cancel()
        self.screen.add_text_box(text, self.layout["text_box"])

    def run(self):
        self.set_background()
        self.set_banner()
        self.timer = wakeup(self.display_text, 0, 2000)

application = Application()
application.run()
