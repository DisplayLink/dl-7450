# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024-2025

from time import strftime
from datastore import ImageStore, KvStore
from splashscreen import Splashscreen, Alignment
from wakeup import wakeup
from dock import DockControl

def set_timezone():
    # Read and set desired timezone from store
    kv_store = KvStore()
    timezone = kv_store.get("timezone")
    dockControl = DockControl()
    try:
        dockControl.set_timezone(timezone)
    except:
        pass

class Screen:
    def __init__(self, image):
        self.screen = Splashscreen()
        self.layout = {}
        image_store = ImageStore()
        image_token = image_store.get_token(image)
        self.screen.set_background(image_token)

    def create_text_box(self, name, text_box_attributes):
        self.layout[name] = text_box_attributes

    def update_text_box(self, name, text):
        self.screen.add_text_box(text, self.layout[name])

class DigitalClock:
    """
    Digital Clock Widget
    """
    def __init__(self, screen, fmt_string):
        set_timezone()
        self.screen = screen
        self.fmt_string = fmt_string
        self.timer = wakeup(self.update, 5000, 1000)
        self.screen.create_text_box("clock", {
            "x": 1890, "y": 30,
            "alignment": Alignment.RIGHT
        })

    def update(self):
        time_str = strftime(self.fmt_string)
        self.screen.update_text_box("clock", time_str)


TIME_FMT = "%H:%M:%S (%Z)\n%d/%m/%Y"
#TIME_FMT = "%c"
#TIME_FMT = "%Y:%m:%d %H:%M:%S"

IMAGE = "screen_3"

clock = DigitalClock(Screen(IMAGE), TIME_FMT)

