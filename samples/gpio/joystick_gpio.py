# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024-2025

from splashscreen import Splashscreen
import gpio

class Joystick:
    PIN_NAMES = [
        "JOYSTICK_CENTER",
        "JOYSTICK_UP",
        "JOYSTICK_DOWN",
        "JOYSTICK_LEFT",
        "JOYSTICK_RIGHT"
    ]

    def __init__(self, on_event):
        self.pins = [
            gpio.create(self.PIN_NAMES[0], callback = lambda: on_event(0)),
            gpio.create(self.PIN_NAMES[1], callback = lambda: on_event(1)),
            gpio.create(self.PIN_NAMES[2], callback = lambda: on_event(2)),
            gpio.create(self.PIN_NAMES[3], callback = lambda: on_event(3)),
            gpio.create(self.PIN_NAMES[4], callback = lambda: on_event(4))
        ]

class Application:
    def __init__(self):
        self.counts = { }
        for n in Joystick.PIN_NAMES:
            self.counts[n] = 0

        self.screen = Splashscreen()
        self.joystick = Joystick(self.on_joystick)
        self.screen.add_text_box(f"Waiting for joystick press...")

    def screen_msg(self, pin_name):
        return f"{pin_name}: {self.counts[pin_name]}"

    def on_joystick(self, direction):
        pin_name = Joystick.PIN_NAMES[direction]
        self.counts[pin_name] += 1
        self.screen.add_text_box(
            self.screen_msg(pin_name)
        )

app = Application()
