.. currentmodule:: mqtt

:mod:`mqtt` --- An MQTT client for IoT services
===============================================

.. module:: mqtt
   :synopsis: functions to enable DL-7450 to be an MQTT client


`Message Queue Telemetry Transport (MQTT) <https://mqtt.org/>`_ is a popular
and widely used messaging protocol for IoT communication. It is an application
layer protocol that operates over the standard TCP/IP stack.  Standard
transport-layer security can be applied. MQTT is a client-to-broker protocol.
Connections are long-lived and bi-directional, or duplex, meaning the the client
can send messages to the broker and vice-versa. It has a built-in *quality of
service* mechanism that ensures that messages are delivered exactly once, at
most once, or at least once, and this can be executed across lost connections.
It provides a *last will and testament* mechanism for when the device goes
offline in an uncontrolled manner (e.g.  power removal). It is suitable for a
constrained, embedded platform such as DL-7450. 

MQTT is supported by many IoT cloud providers such as Azure Iot Hub, and is
also a popular choice for bespoke IoT cloud backends. It is the mechanism we
use for communicating with our development backend, and the delivery mechanism
for Python code for the Workshop. We have validated and demonstrated that it
supports Azure Iot Hub applications, using the Device twin and application
message mechanisms. We have shown that in-field firmware updates can be managed
through both Azure IoT hub and our backend development server.

More information about the MQTT protocol can be found at https://mqtt.org/

Constants
---------

The following *quality-of-service* constants for the MQTT protocol are defined
in the :py:mod:`mqtt` module. The QOS level is used by the client when
publishing messages and by the server when sending messages on subscribed
topics. The optional *will message* also has an associated QOS.

.. data:: QOS0 
   
   This is service-level *at most once*, or *fire and forget*. The sender waits
   for no acknowledgements of receipt and makes no attempt to resend the
   message.

.. data:: QOS1

   This is service-level *at least once*. The sender expects an acknowledgement
   of receipt and will retry sending after a time defined in the connect
   options. The message may eventually be received multiple times.

.. data:: QOS2

   This is service-level *exactly once*. A four-step handshake is used to
   ensure that the message is received exactly once.


Functions
---------

.. function:: ErrorDescription(errno: int) -> str
   
   Returns a string containing a human-readable description of an MQTT error
   code.


Classes
-------

.. toctree::
  :maxdepth: 1

  mqtt.Client.rst
  mqtt.MqttError.rst
