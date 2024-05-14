# MQTT

The DL-7450 has the capability to communicate with an MQTT broker, enabling the
DL-7450 to subscribe to particular topics and send & receive messages.

A [sample app](mosquitto.py) has been provided that demonstrates connecting to
the Eclipse Mosquitto test MQTT broker. Information on how to use this broker
can be found at https://test.mosquitto.org/.

The provided app connects to the test broker on port 8886, which is encrypted
using a certificate signed by the Let's Encrypt CA. It then subscribes to a
topic based on the dock ID of the chip, and periodically sends messages on this
topic. The splash screen will display the events taking place as they occur.

There are a number of changes that can be made to the sample app, including:

* Connecting to the broker on different ports, which require connecting over
  different protocols or providing different levels of authentication and/or
  encryption.
* Subscribing to different topics.
* Sending different messages over different topics.


It is suggested to connect multiple DL-7450 chips (and/or non-DL-7450 clients)
to the MQTT broker, and investigating how these clients influence the sending
and receiving of messages.
