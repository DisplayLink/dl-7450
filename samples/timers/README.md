# Task scheduling using the DisplayLink DL-7450 SDK

The DL-7450 is an embedded, and therefore, resource-constrained platform.
Customer applications run on a single *application thread*. This requires a
certain discipline and style of coding. The application's `main` function
should run quickly and do very little work besides setting up mechanisms for
handling small tasks periodically during the normal operation of the dock.

Task handling falls into two broad categories.

 * Tasks scheduled on a timer. The DL-7450 *wakeup* module supports several
   styles of task scheduling. First, a task can be scheduled to run a number of
   milliseconds from now. For example, you may want to set an alarm to notify a
   hotdesk user that their booking is nearly up. Alternatively, you may set a
   retry timer when an HTTP server suggest trying a request again after some
   seconds.
   
   The `wakeup` library also allows applications to set repeating timers to run
   a task many times at a given frequency. For example, an application may wish
   to poll a system state periodically, to fetch new content from an external
   provider every once in a while or to blink an LED every 500ms. 

 * Work that happens in response to events. For example the DL-7450 *DockEvent* interface
 enables applicaitons to register handlers for events such as monitor disconnect, or USB 
 peripheral plugs. Event handling is also used for peripheral control libraries that are not
 available in this preview, including general pin input/output (GPIO) events (e.g. button
 handling).

This tutorial shows how to develop a [digital clock widget](clock.py), perhaps
to embed in a larger application.  To create a digital clock, it might be
tempting to write something like this:

 ```python
def update_clock(now):
    # update the splashscreen clock

while True:
    now = time.localtime()
    update_clock(now)
    sleep(1.0)
 ```

However, this approach starves the application thread, and does not give the
Python runtime a chance to carry out other tasks, including unloading and
reloading application code, or to allow your application to run different tasks
concurrently. An alternative approach is to create a *repeating timer* using
the DL-7450 `wakeup` library.

```python
class DigitalClock:
    def __init__(self, on_time_change):
        self.timer = wakeup(self.update, 0, 1000)

    def update(self):
        now = localtime()
        # update splashscreen clock

```

The `wakeup` function takes three parameters. The first is a task, which is any
callable Python entity.  The second is the *delay from now in milliseconds* for
the task to be executed. The third parameter is an optional *repeat time*, i.e.
how often to repeat the task. Omitting this parameter creates a one-shot timer.
This approach leaves the application thread idle most of the time, allowing
applications, or the Python runtime to carry out other tasks.

## Suggested walkthrough

While the primary objective of this tutorial is to show how to create timers,
the [digital clock widget](clock.py) also shows how the DL-7450 implementation
of the standard time module can be used. It also shows that the *DockControl* interface can be used to set the dock's timezone.

 * Change the line where the timezone is set to another of the supported timezones, e.g. 

   ``` python
   dockControl.set_timezone("GMT")
   ```
   
   reload the application and observe the timezone change. NB, the timezone
   is now set until another call changes it again, including when another
   application is loaded. In practice, an application should not assume the
   timezone, but should set it.
 
 * Try the different 

 * While a one-second frequency clock is useful to demonstrate the timer
   functionality, in practice a clock that updates on the minute is more
   likely. See if you can change the code to poll the time every second, but
   only update the screen if the time has changed since the last update. 
