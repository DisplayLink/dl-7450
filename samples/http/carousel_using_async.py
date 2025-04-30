# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024-2025

import http
import json
from wakeup import wakeup
from splashscreen import Splashscreen

# UK South Data Centre
# CONTENT = "https://6pantherpublicanonymous.blob.core.windows.net/dl-7450/content.json"
CONTENT = "https://6pantherpublicanonymous.blob.core.windows.net/dl-7450/content2.json"

# Asia Data Centre
# CONTENT = "https://sdkworkshop.blob.core.windows.net/dl-7450/content.json"
# CONTENT = "https://sdkworkshop.blob.core.windows.net/dl-7450/content2.json"


class Carousel:
    # Keep the timer in scope, so it doesn't get garbage collected.
    timer = None
    splashscreen = Splashscreen()

    def __init__(self, url):
        response = http.get(url)
        if response.status_code() != 200:
            raise Exception("Error getting content")

        content = json.loads(response.body())
        self.base_url = content["data"]["base_url"]
        self.items = content["data"]["images"]
        self.next()

    def next(self):
        http.get_async(self.base_url + self.items[0], self.set_background)
        self.items = self.items[1:] + self.items[:1]

    def set_background(self, response):
        if response.status_code() != 200:
            raise Exception("Error getting content")

        self.splashscreen.set_background(response.body())
        self.timer = wakeup(self.next, 5000)


carousel = Carousel(CONTENT)
