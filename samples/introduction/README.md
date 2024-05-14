# Introduction

In the preview workshop for the DisplayLink DL-7450 SDK, this is the [default
application](default.py) that is running on the dock. The application is
straightforward, but showcases many of the DL-7450 capabilities that are
available to application developers.

## Python Applications

First, we see that the dock is running an application, coded in a variant of
the Python language based on [micropython](https://micropython.org/). A subset
of the standard Python modules are available, such as `builtins`, `time`,
`json`. DL-7450 is a resource-constrained platform, so we have made some
choices as to whether to include a module based on its size and whether it
supports particular use cases. In addition to the core modules, the SDK
provides modules that are specific to the management and control of the DL-7450
docking chip. We will look at some of these modules through these sample
applications.

For the SDK preview workshop, new applications can be deployed to the dock from
a web interface. The front end submits the code via a REST endpoint in the
Synaptics development cloud, and is propagated over a secure
[MQTT](https://mqtt.org/) link to the DL-7450. When the new code is received,
the dock stops the existing application in an orderly fashion and runs the new
application.

If there are any coding mistakes, such as syntax errors, or any unhandled
runtime exceptions, the Python engine will unload the application code and
report the error on the DL-7450 splashscreen as a stack trace. The error can be
corrected and the new version of the code can be loaded at this point.

Let's look at some of the capabilities that are showcased in this application.

## Data storage

The DL-7450 contains a non-volatile (persistent) flash storage areas. There is
a factory storage area that is populated in the customer factory. It contains
application data, such as the factory Python application, images for
constructing splash screens and any data that the application may need,
including dock-specific data. The factory data is immutable, and will always be
available even on factory reset of the device.

There is a further non-volatile storage area that can be populated by
applications at runtime. This might include an updated version of the customer
Python application or data that has been computed or obtained by the
application, such as tokens for connecting to a cloud service.

There is a final storage area that the application can use at runtime. This is
for *ephemeral* data, which will be lost on a reboot of the dock. It can be
used for storing data such as current splash screen content. Using this area
means that the application does not need to expend the Python runtime memory
heap.

The DL-7450 SDK provides mechanisms for storage and retrieval of data in the
various areas. There is a dedicated *ImageStore*, where applications can save
image data and reference it by an *ImageTag*. This allows the Python
application to refer to an image, without having to copy it into the Python
heap until it is really needed, if at all. Other data types can be stored in a
*Key-Value* storage area. All Python built-in types such as strings,
dictionaries and lists can be stored in the *KvStore*. Data might include the
URL of a content-provider endpoint, or a user-friendly identity for the dock.
The `datastore` module provides policies for data-retrieval. For example, the
application may prefer to use data in the ephemeral store, over the
non-volatile runtime store, over the factory store.  

**NOTE** In this preview, only the factory storage area is available. In the
DL-7450s used for the preview workshop, the factory data store has been
populated with a few splashscreen images, and some per-dock data, such as a
dock friendly name and the preferred timezone. The [default workshop
application](default.py) is also stored in the factory data store. When the
dock boots it will load and run this application.

## Splashscreen rendering
The preview of the DL-7450 SDK contains a simple library for rendering
splashscreen images. The splashscreen background can be selected. In the
[present application](default.py) the image data is retreived from the factory
data storage area. In later tutorials, splashscreen data will be pulled from an
off-dock source by the DL-7450 or else pushed to the DL-7450 by a management
application running on a local network or in a cloud service.

## Dock management information
This application also uses the network module to retrieve and display the IP address of
the dock. Later tutorials will explore the range of management functionality available
for the DL-7450.

## Task scheduling
The final capability used in the [default application](default.py) is a *wakeup* timer. The timer is used to schedule tasks, or units of work. In this application, a timer is created to check periodically whether the dock is connected to the internet or not. Once the connection is established, the dock displays the IP address and cancels the timer. The [timer tutorial](../timers/README.md) explains the `wakeup` library in more detail.

## Suggested walkthrough

 * Observe the dock in its default state. There should be a splashscreen
   background and some informative text lines.
 * Read the [application code](default.py). Change the line that loads the
   splashscreen background image from 

   ```python
   background = "default"
   ```

   to

   ```python
   background = "screen_2"
   ```
   and reload the code. Observe a different splash screen background
   loading.

 * Make a deliberate error in the code, e.g.

   ```python
   application.urn()
   ```

   The application will fail and the screen will show the stack trace. Fix
   the error, reload, and observe the application working again.

 * Change the text displayed. E.g. change

   ```python
   ip, _, _, _ = self.nic.ifconfig()
   .
   .
   .
   text.append(f"IP Address: {ip}")
   ```

   to

   ```python
   mac_address = self.nic.mac_address()
   .
   .
   .
   text.append(f"MAC Address: {mac_address}")
   ```
 
 * Experiment with the markup tags. For example, change the span attributes of the banner:
        
   ```python
   banner = "<span foreground=\"red\"><b>Welcome to the DisplayLink DL-7450 SDK Workshop</b></span>"
   ```

