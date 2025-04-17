.. currentmodule:: mqtt
.. _mqtt.MqttError:


class MqttError
===============

Represents an error during an MQTT operation.

.. class:: MqttError()

   .. attribute:: errno: int

      This table gives some of the possible error codes. For debugging
      purposes, the `mqtt.ErrorDescription` function can be used to obtain a
      human-readable version of the error code. 
      
      +---------------+----------------------------------------------------------+
      | errno         | Meaning                                                  |
      +===============+==========================================================+
      | 0             | No error                                                 |
      +---------------+----------------------------------------------------------+
      | -1            | Generic error                                            |
      +---------------+----------------------------------------------------------+
      | -2            | Persistence error                                        |
      +---------------+----------------------------------------------------------+
      | -3            | The client is disconnected                               |
      +---------------+----------------------------------------------------------+
      | -4            | The maximum number of in-flight messages reached         |
      +---------------+----------------------------------------------------------+
      | -5            | Invalid UTF-8 string                                     |
      +---------------+----------------------------------------------------------+
      | -6            | Invalid None value provided                              |
      +---------------+----------------------------------------------------------+
      | -9            | Invalid QOS value                                        |
      +---------------+----------------------------------------------------------+
      | -10           | No more message IDs                                      |
      +---------------+----------------------------------------------------------+
      | -14           | Bad protocol in URL                                      |
      +---------------+----------------------------------------------------------+

   .. attribute:: args: List
   
      Further arguments for the error. At present only *args[1]* is used, and is
      a human-readable string describing the error. Please note, *MqttError.args[0]*
      is equivalent to *MqttError.errno*.


