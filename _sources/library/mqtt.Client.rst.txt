.. currentmodule:: mqtt
.. _mqtt.Client:

class MqttClient -- communicate with an MQTT broker
===================================================

The `MqttClient` class provides the functionality to enable the DL-7450 to
become an MQTT client. All of the methods are implemented asynchronously, i.e.
the call returns control to the application quickly, and informs the
application through relevant callbacks about MQTT events.


.. class:: MqttClient(broker_url: str, client_id: str)

   Create an MQTT client class that is able to connect to the given broker. The
   client is created in a ready-to-connect state and the actual connection is
   initiated in the `MqttClient.connect` call. If this call fails an
   `MqttError` will be generated.

   The arguments to this constructor are:

     - *broker_url* is the address of the MQTT broker, in the usual form
       *scheme://host:port*. The scheme must be one of the values below,
       otherwise an error is raised. The host can be either an IP address or a
       host name. If omitted, the default port listed below will be used.
     - *client_id* is a mandatory UTF-8 encoded string containing the MQTT client ID.

   +------------+----------------------------------+--------------+
   | URL Scheme | Connection Type                  | Default Port |
   +============+==================================+==============+
   | ``tcp``    | Insecure MQTT                    | 1883         |
   +------------+----------------------------------+--------------+
   | ``mqtt``   | Insecure MQTT                    | 1883         |
   +------------+----------------------------------+--------------+
   | ``ssl``    | Secure MQTT                      | 8883         |
   +------------+----------------------------------+--------------+
   | ``mqtts``  | Secure MQTT                      | 8883         |
   +------------+----------------------------------+--------------+
   | ``ws``     | MQTT over insecure websocket     | 80           |
   +------------+----------------------------------+--------------+
   | ``wss``    | MQTT over secure websocket       | 443          |
   +------------+----------------------------------+--------------+

  .. admonition:: Preview feature

    Web sockets are provided as a preview feature in this version of the DL-7450
    SDK. Please get in touch to provide feedback or report any issues.


  .. method:: connect(on_connect, options = {})
  
    This method initiates a connection to the broker. The connection occurs
    asynchronously, and informs the application when the connection has succeeded
    or failed. 

    The *on_connect* argument is any callable entity which takes two arguments.
    The first argument is an integer, *rc* which indicates whether the broker
    accepted the connection or not. A zero or positive value is the value
    returned from the broker, and the meaning is given in the table below.

    +----------+-------------------------------------------------+
    | Status   | Reason                                          |
    +==========+=================================================+
    | 0        | Connection Accepted                             |
    +----------+-------------------------------------------------+
    | 1        | Connection Refused, unacceptable MQTT protocol  |
    +----------+-------------------------------------------------+
    | 2        | Connection Refused, identifier rejected         |
    +----------+-------------------------------------------------+
    | 3        | Connection Refused, server unavailable          |
    +----------+-------------------------------------------------+
    | 4        | Connection Refused, bad user name or password   |
    +----------+-------------------------------------------------+
    | 5        | Connection Refused, not authorised              |
    +----------+-------------------------------------------------+

    A negative value indicates that the connection attempt was not initiated for
    some reason, and the value corresponds to one of the values of the
    `MqttError` codes. The second argument, *flags* is a dictionary and is
    unused in the present version of the DL-7450 SDK.  The callback is invoked
    asynchronously, when the connection is established, or when a connection
    cannot be established for some reason. 

    Example callback function::

      def on_connect(rc, flags):
        if rc == 0:
          # connection accepted by the broker
        else:
          errMsg = mqtt.ErrorDescription(rc)
          # report or handle error.


    *options* is a dictionary that contains a variety of optional parameters
    for this connection. The possible key-value pairs are described below. All
    are optional with default values, but some combinations of the options are
    invalid.

    **Connect Options:**

    .. csv-table::
      :header: "Option", "Description"
      :widths: 3, 10
      :align: left

      "*keep_alive*", "The time, in seconds, between attempts by the server
      (PING requests) to establish whether the client is unresponsive or
      disconnected. If this value is omitted, the keep alive mechanism is not
      enabled."
      "*username*", "This is the MQTT username and must be a valid UTF-8
      string. If *username* is provided, *password* may be omitted. A
      *password* with no *username* is not allowed."
      "*password*", "This is the MQT password. The password must be a valid
      string, bytes or bytearray. If *username* is provided, *password* may be
      omitted. A *password* with no *username* is not allowed."
      "*will_topic*", "This must be a valid UTF-8 string representing the topic
      for the will message to be published on. This option forms part of the
      will message and if not provided or is *None*, then no will message is
      defined."
      "*will_qos*", "This must be a valid *will_qos*, i.e. an integer 0, 1 or
      2. This option forms part of the will message and if not provided or is *None*, then no will message is defined."
      "*will_message*", "The payload, *will_message*, maybe empty or None, or a
      string, bytearray or bytes object. This option forms part of the will
      message and if not provided or is *None*, then no will message is
      defined."

    **Secure Sockets Layer (SSL) options:**

    .. csv-table::
      :header: "Option", "Description"
      :widths: 3, 10

      "*trust_store*", "The broker certificate's chain-of-trust in PEM or DER
      form. If provided must be a valid string, bytearray or bytes."
      "*private_key*", "The client's private key in PEM format, used when the
      broker requires client certificate authentication. Must be a valid
      string, bytearray or bytes object"
      "*key_store*", "The client's public certificate chain in PEM format. Must
      be a valid string, bytearray or bytes object. May include the private
      key, or the private key may be provided separately."

    With the preceding constraints, any of options may be omitted or None, and
    their default values will be used. The presence of an unrecognised option
    will lead to a *TypeError* being raised.

  .. note::
      
      The *clean_session* option is currently set to 0 and cannot be changed in
      this version of the DL-7450 SDK.

  .. method:: publish(topic, message, qos)

     This method initiates the publication of a message to the broker. The
     parameters are:

       - *topic* a valid UTF-8 string that is the topic the message will be
         published on.
       - *message* the payload of the MQTT message. It must be a valid string,
         bytearray or bytes object.
       - *qos* the quality-of-service level for this message.

     This call will raise a *TypeError* if the parameter combination does not
     define a valid MQTT message. In particular, a zero-length topic is not
     allowed, and *qos* must be an integer 0, 1 or 2. The *message* can be
     empty.

     The return value is an integer, *mid*, which is an identifier for the message
     just published. It is used in the *on_publish* callback to identify which
     messages have been successful or unsuccessful.

     Example usage::

        from mqtt import MqttClient
        import json

        client = MqttClient('ssl://my.broker:8883', 'myclientid')
        client.connect(...)

        payload = {
          'status': 42
        }

        mid = client.publish(f'/device/status{myclientid}', json.dumps(payload), 1)

     If this method is called on a disconnected client, the message will be
     sent when the client next becomes connected. However the message will be
     lost if the client goes out of scope (e.g. via a reboot of the DL-7450).


  .. method:: subscribe(topics)

     This methods initiates a subscription to one or more topics. The parameter
     *topics* is a single 2-tuple or a list of 2-tuples, where each 2-tuple is
     of the form *(topic, qos)*. The topic must be a valid, non-empty, str,
     which may contain valid topic wildcards. *qos* is an integer 0, 1 or 2,
     indicating the quality-of-service required for the subscription.

     The return value is an integer: a negative value indicates that the
     subscription attempt was not initiated for some reason, and the value
     corresponds to one of the values of the `MqttError` codes.  A positive
     value is a message identifier, *mid*, which identifies the subscription
     request. It is used in the *on_subscribe* callback to refer back to which
     topics have been subscribed to. Subscriptions are often set up in the
     *on_connect* callback following a successful connection to a broker.

  .. method:: on_message(callback)
     
     Set up a handler function for messages that the client receives on its
     subscribed topics.  Please note, if the client will only publish messages
     then it is not necessary to set up a message handler. The *callback* is
     any Python callable entity that takes two parameters, the topic that the
     message has been sent on, and the message itself, as a bytearray. The
     application should interpret the bytearray appropriately.  For example::

       from mqtt import MqttClient
       import json

       def on_message(topic, message):
          if topic == "/urgent/maintenance":
             my_msg = json.loads(message) 
             # etc

       client = MqttClient('ssl://mybroker.com:8883')
       client.on_message(on_message)

  .. method:: on_subscribe(callback)
     
     Register a callback that is invoked when the broker responds to a
     subscribe request. The *callback* is a callable entity that takes two
     arguments. The first is an integer, *mid*, which corresponds to the
     message identifier that was returned by the `MqttClient.subscribe` call.
     The second argument, *granted_qos* is a list of integers corresponding to
     the quality-of-service granted for each of the subscriptions in the
     request. 
     
