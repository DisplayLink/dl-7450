# DisplayLink DL-7450 SDK Samples

These samples provide an introduction and tutorial to the preview of the
DisplayLink DL-7450 Software Development Kit. The DL-7450 is able of running
Python applications, enabling manufacturers to create differentiated enterprise
docking solutions, built on the extended capabilities of the DL-7450 silicon.
We suggest following the samples in order, and studying the README file for
each sample. Each sample contains a README.md file, a main python application
and in some cases related examples. 

The samples are chosen to showcase the capabilities of the DL-7450 that are
exposed through the SDK. Each code sample is deliberately short and focusses on
one or two capabilities. See the 
[API documentation pages](https://displaylink.github.io/dl-7450/)
for a full guide to the SDK.

1. [Introduction](introduction/)
2. [Dock Management](dock_management)
3. [Task scheduling](timers)
4. [Interacting with the web](http)
5. [Internet of Things](iot) 
6. [GPIO](gpio)
7. [I2C](i2c)
8. [MQTT](mqtt)

Follow the instructions in the scripts folder to send sample code to your DL-7450 and 
for sending content to the Internet of Things sample apps.

NOTE: these samples require application ROM store data to be present. See the
[helper scripts](scripts/README.md) for details on how to modify and restore
the dock's application ROM store.
