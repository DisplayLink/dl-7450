# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024-2025

from splashscreen import Splashscreen
import gpio

PIN_NAME = "JOYSTICK_CENTER"

class Button:
    def __init__(self):
        self.press_count = 0
        self.pin = gpio.create(PIN_NAME, callback=self.cb)
        self.screen = Splashscreen()
        self.screen.add_text_box("Waiting for button press...")

    def screen_msg(self):
        return f"PinName : {PIN_NAME}\nPressed {self.press_count} times"

    def cb(self):
        self.press_count = self.press_count+1
        self.screen.add_text_box(self.screen_msg())

pin = Button()

