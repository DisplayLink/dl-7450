# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024-2025

import http
import json
from wakeup import wakeup
from splashscreen import Splashscreen

# uk south datacentre
#CONTENT = "https://6pantherpublicanonymous.blob.core.windows.net/dl-7450/content.json"
#CONTENT = "https://6pantherpublicanonymous.blob.core.windows.net/dl-7450/content2.json"

# Asia datacentre
#CONTENT = "https://sdkworkshop.blob.core.windows.net/dl-7450/content.json"
CONTENT = "https://sdkworkshop.blob.core.windows.net/dl-7450/content2.json"

class ContentProvider:
    def __init__(self, url):
        response = http.get(url)
        if response.status_code() != 200:
            raise Exception("Error getting content")

        content = json.loads(response.body())
        self.base_url = content["data"]["base_url"]
        self.items = content["data"]["images"]

    def next(self):
        response = http.get(self.base_url + self.items[0])
        self.items = self.items[1:] + self.items[:1]
        if response.status_code() == 200:
            return response.body()


class Carousel:
    def __init__(self, content):
        self.content = content
        self.splashscreen = Splashscreen()
        self.timer = None

    def show_next(self):
        background = self.content.next()
        if background:
            self.splashscreen.set_background(background)

    def start(self):
        self.timer = wakeup(self.show_next, 0, 5000)

content = ContentProvider(CONTENT)
carousel = Carousel(content)
carousel.start()


