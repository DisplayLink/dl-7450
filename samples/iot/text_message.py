# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) 2024 DisplayLink (UK) Ltd.

from datastore import ImageStore
from vision_client import VisionClient
from splashscreen import Splashscreen, Alignment


class Application:
    layout = {
        "text_area": {
            "x": 960, "y": 700,
            "alignment": Alignment.MIDDLE
        }
    }

    def __init__(self):
        self.client = VisionClient()
        self.screen = Splashscreen()

    def show_text(self, message):
        self.screen.add_text_box(message, self.layout["text_area"])

    def run(self):
        images = ImageStore()
        image_token = images.get_token("screen_2")
        self.screen.set_background(image_token)
        self.show_text("Waiting for message..")
        self.client.on_message(self.handle_message)

    def handle_message(self, message):
        messageType = message[0]
        message = message[1:]

        # Check messageType is "t"
        if messageType == 116:
            self.show_text(str(message, "utf-8"))

app = Application()
app.run()

