.. currentmodule:: vision_client
.. _vision_client.VisionClient:

class VisionClient
==================

The VisionClient class enables DL-7450 to communicate with a development IoT
backend. To use this mechanism, the application developer must first register
an account with the backend and then register the development board to that
account. Please contact Synaptics if  you would like to create such an account.

The IoT development platform provides a REST API for sending free-form
application messages to a DL-7450. The VisionClient class enables the DL-7450
application to receive and process these messages. 

Constructors
------------

.. class:: VisionClient()

   Construct a DockControl object.

Methods
-------

.. method:: VisionClient.on_message(callback)

   Register a callback handler for application messages. The message is
   delivered as a `bytearray` and has no meaning except to the application. The
   callback must interpret the message. For example if the message was sent
   through the development IoT REST api as string encoded into an array of
   bytes, the handler could be implemented as follows::

      from vision_client import VisionClient
      from splashscreen import Splashscreen

      client = VisionClient()
      screen = Splashscreen()

      def callback(message):
        screen.add_text_box(str(message, 'utf-8'))

      client.on_message(callback)

.. method:: VisionClient.send_message(msg)

   Not available in this preview.
