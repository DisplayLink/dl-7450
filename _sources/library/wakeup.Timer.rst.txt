.. currentmodule:: wakeup
.. _wakeup.Timer:

class Timer -- schedule tasks
=============================

The *Timer* class represents a piece of work, or a task, to be performed later,
and perhaps repeatedly at a given interval. The DL-7450 will "wake up" and
perform the specified task. For instance, an application developer may want to
create a weather report to show on the DL-7450 splashscreen that is updated
every ten minutes::

    from wakeup import Timer

    def update_weather():
      # perform an HTTP request and update a widget on the
      # splashscreen
      pass

    timer = Timer(update_weather, 0, 10*60*1000)


Constructors
------------

.. class:: Timer(task, time_ms, repeat_ms = 0)

   Schedule a task to be carried out later. The parameters are:

      - *task*: a callable entity that takes no parameters.
      - *time_ms*: the time delay from now at which to perform the task in milliseconds. 
        This value can be set to 0 to perform the task immediately.
      - *repeat_ms*: if this value is non-zero, the task will be performed again every this
        many milliseconds. 

   .. method:: Timer.cancel()

      Cancel the timer.


