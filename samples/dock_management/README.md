# Dock management

In this tutorial we see how to capture and show information about the DL-7450 
in real-time. This capability underpins more realistic and valuable use cases for 
differentiated products. We mention two here.

## DockEvent class
Currently, this preview does not yet expose an important management class, the DockEvent interface. This
enables application developers to be notified of events, rather than polling for them. Generally,
triggering event callbacks leads to better user experience that periodically
polling for changes.


## Reacting to host status changes

```python
from dock import DockEvent, HostStatus
from splashscreen import Splashscreen

screen = Splashscreen()
events = DockEvent()

def on_host_status(status):
  if status == HostStatus.NoDriver:
     screen.add_text_box("Install DisplayLink drivers")
  elif status == HostStatus.Connected:
     # e.g. suspend screen operations
     pass
  else:
     # e.g. resume screen operations

events.on(HostStatus, on_host_status)

```

## Internet-of-Things device management
An IoT provider, such as Azure IoT hub, can be used for asset tracking and management. An IoT
application may want to know what peripherals are connected to the dock. For example in a hot-
desking scenario, a user may want to know if a desk has a 4K monitor, or two monitors. An
IT manager may want to ensure a desk is ready to use, and has a monitor, mouse and keyboard
attached. The hot-desking application can also infer whether a desk is in use according to
whether a host PC or laptop is tethered to the dock.

The following sample will not run in this preview, but is provided as an illustration
of how application developers might use a released version of the DL-7450 SDK.

```python
from dock import DockInfo
import usb
from iot.utils import AzureIotClient

client = AzureIotClient(...)

def update_iot_provider()
    info = DockInfo()

    host_status = info.host_status()
    monitors = info.monitors()

    # detect by VID/PID
    mouse = usb.find(vid=0x0101, pid=0x4242)

    client.update_device_twin({
      "host_status": host_status,
      "monitor_modes": [m.preferred_mode() for m in monitors],
      "mouse_present": (mouse != None)
    })

```

## Mounting a USB file system

```python

# If a USB flash drive is connected mount the filesystem


```


## Suggested walkthrough

 * change filter
