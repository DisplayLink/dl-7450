# iperf

The DL-7450 has the capability to run as an iperf client, allowing for network
bandwidth testing of the DL-7450 system.

A [sample app](iperf_client_runner.py) has been provided that demonstrates
connecting to a running iperf server. The code expects the server to exist at
the `iperf-server` hostname at port 5000, but these can both be changed by
modifying the `SERVER_NAME` and `SERVER_PORT` variables respectively.

After connecting to the server, the app will run a standard iperf test over 5
intervals. The splash screen will display the speeds recorded by the app, as
well as any errors that have occured.

It is worth exploring the different fields that can be parsed out of the
JSON passed into `_display_result`.
