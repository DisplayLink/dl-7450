.. _dl_7450_quickref:

Quick reference
===============

Below is a quick reference for the DL-7450 SDK. 


Schedule tasks
--------------

Use the :ref:`wakeup <wakeup.Timer>` class to scheule tasks::

    from wakeup import Timer

    timer1 = wakeup.Timer(task, 60*1000)  # schedule a one-off task in 60 seconds time
    timer2 = wakeup.Timer(task, 0, 1000)  # schedule a task to repeat every second


Dock information
----------------

Use the :ref:`DockInfo <dock.DockInfo>` class to obtain current dock information::

    from dock import DockInfo

    info = DockInfo()                # obtain a dock information object
    info.dock_id()                   # obtain the unique dock identifier
    info.monitors()                  # obtain the connected monitor details

Dock control
------------

Use the :ref:`DockControl <dock.DockControl>` class to control dock settings::

    from dock import DockControl

    control = DockControl()          # obtain a dock control object
    control.set_timezone("GMT")      # set the dock timezone

Splashscreen control
--------------------

Use the `splashscreen` module to control the splash screen content::

    from splashscreen import Splashscreen, Alignment
    import image

    screen = Splashscreen()                             # create a splash screen control interface
    screen.set_background(bg_image, image.PNG)          # set the splash screen background
    screen.add_text_box(["Hello, world"])               # create text box in default message position

    text_attributes = {                                 # control the position of text
      "x": 300,
      "y": 200,
      "alignment": Alignment.RIGHT
    }
    screen.add_text_box(["Welcome!"], text_attributes)  # create text box with attributes


HTTP requests
-------------

Use the `http` module to perform HTTP requests::

    import http

    response = http.get("http://example.com")  # make an HTTP GET request

