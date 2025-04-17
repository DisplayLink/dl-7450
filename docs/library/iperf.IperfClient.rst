.. currentmodule:: iperf
.. _iperf.IperfClient:

class IperfClient -- run iperf3 tests as client
===================================================

The `IperfClient` class enables the DL-7450 to become an iperf3 client.
The `IperfClient.run` method is implemented asynchronously, i.e.
the call returns control to the application quickly, and informs the
application of the iperf3 test results through a callback.

In order to fully utilise this test, an iperf3 server must be set up on another
machine. After installing or otherwise obtaining a copy of iperf3 on the other
machine, run the iperf3 server::

  iperf3 -s -p <port>

This server can now be connected to with the `IperfClient`.


.. class:: IperfClient(hostname: str, port: int)

  Create an iperf3 client class that connects to the given hostname at the given
  port. The client is created in a ready-to-connect state and the actual
  connection is initiated in the `IperfClient.run` call.

  The arguments to this constructor are:

  - *hostname* is the address of the iperf3 server. The hostname can be either an
    IP address or a traditional host name.
  - *port* is the port number that the iperf3 server is running on.


  .. method:: run(on_complete: Callable[[dict], None] = None)

    This method initiates a connection to the iperf3 server and runs an iperf
    test asynchronously.

    The *on_complete* argument is any callable entity which takes a
    dictionary *result* as an argument. Upon completion of the iperf3 test,
    the *on_complete* callback is called, with the JSON output parsed and
    passed in as the *result* argument.

    For an example of what output can be expected, see the output of a
    standard iperf3 call::

      iperf3 -c <hostname> -p <port> -t 10 --json

    and inspect the avaiable JSON fields.

    Just as with the standard iperf3 client, the `IperfClient.run` method will
    still return failures in JSON format, but with the ``error`` field set.

    In the event of a non-iperf error, or if iperf cannot generate any JSON
    output, the `IperfClient.run` method will return an empty dictionary.
