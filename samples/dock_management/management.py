# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024

from datastore import ImageStore
from dock import DockInfo
from splashscreen import Splashscreen, Alignment
import usb
from wakeup import wakeup

# Filter out the USB2 and USB3 hubs from the 
USB_FILTER = [
  (0x1d6b, 0x0002),
  (0x05e3, 0x0610),
  (0x1d6b, 0x0003),
  (0x05e3, 0x0625)
]

# Outputs 0-3 on the Redwood development board
OUTPUT_TYPES = ["HDMI", "DP", "HDMI", "DP"]

class PeripheralsPage:
    def __init__(self, screen):
        self.screen = screen
        self.dock_info = DockInfo()
        self.layout = {
            "central": {
                "x": 540, "y": 300,
                "alignment": Alignment.MIDDLE
            }
        }

    def add_text_box(self, text):
        self.screen.add_text_box(text, self.layout["central"])

    def fmt_usb_device(self, device):
        vid, pid, name = device
        return f"<span size=\"small\">{vid:04x}:{pid:04x} {name}</span>"

    def fmt_monitor(self, idx, monitor):
        if monitor.valid():
            x, y = monitor.preferred_mode()
            return f"<span size=\"small\"><b>{idx+1}: </b> ({OUTPUT_TYPES[idx]}) {monitor.name()} {x}x{y}</span>"
        else:
            return f"<span size=\"small\"><b>{idx+1}: </b> Not connected...</span>"

    def usb_devices(self):
        # Filter out the hubs.
        devices = usb.find()
        connected = []
        for device in devices:
            if (device[0], device[1]) not in USB_FILTER:
                connected.append(device)
        return connected


    def update(self):
        text = ["<b><span size=\"small\">Connected USB peripherals</span></b>"]
        text = text + [
            self.fmt_usb_device(device)
            for device in self.usb_devices()
        ]

        text = text + ["", "", "<b><span size=\"small\">Monitors</span></b>"]
        monitors = self.dock_info.monitors()
        text = text + [
            self.fmt_monitor(idx, monitor)
            for idx, monitor in enumerate(self.dock_info.monitors())
        ]

        self.add_text_box(text)

class Application:
    def __init__(self):
        self.screen = Splashscreen()
        images = ImageStore()
        image_token = images.get_token("default")
        self.screen.set_background(image_token)

        self.page = PeripheralsPage(self.screen)
        self.timer = None

    def run(self):
        self.timer = wakeup(self.page.update, 5000, 1000)

app = Application()
app.run()

