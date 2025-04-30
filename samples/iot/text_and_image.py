# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) 2024-2025 DisplayLink (UK) Ltd.

import vision_client
from splashscreen import Splashscreen

visionClient = vision_client.VisionClient()
screen = Splashscreen()

def cb(message): 
  mv = memoryview(message)
  messageType = mv[0]
  message = mv[1:]

  # Check messageType is "i"
  if messageType == 105:
    screen.add_text_box("Loading Image..")
    screen.set_background(message)
    screen.add_text_box("")
  # Check messageType is "t"
  elif messageType == 116:
    screen.add_text_box(str(message, "utf-8"))

visionClient.on_message(cb)
screen.add_text_box("Waiting for instruction...")