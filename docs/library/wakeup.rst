:mod:`wakeup` --- functions for running code at a specific time 
===============================================================

.. module:: wakeup
   :synopsis: schedule one-off or repeated tasks on the DL-7450

This module provides a general timer that triggers the DL-7450 to carry out a
task after a specified amount of time has elapsed. It is possible to create a
*repeating* timer, i.e. one that repeats the task periodically. Timers can also
be cancelled. Use cases include:

   - Retrying an operation after a few seconds. For example, if you make an
     HTTP request which responds with a ``Retry-After`` header, you can use a
     timer to schedule the retry attempt.
   - Set up a polling mechanism to check for some state of affairs every few
     seconds. For example you may have a temperature sensor and you check the
     temperature every minute.
   - You may have some screen content that you want to update every few
     seconds. 
   - You may wish to send a report to your cloud service provider every night. 

As described in the :ref:`programming paradigm <dl_7450_paradigm>`
documentation, it is expected that your application main function will do very
little work except for setting up timers and event handlers. The
:py:class:`Timer` supports this paradigm.

.. warning::
   If there are no references to a Timer, the Python garbage collector may
   destroy it at any time. It is the responsibility of the application to make
   sure that timers are not referenced to keep them active. For example::
      
      from wakeup import wakeup
      
      # bad - timer may be garbage collected
      wakeup(update_clock, 0.0, 1.0) 

      # Better. Timer kept in scope.
      my_timer = wakeup(update_clock, 0.0, 1.0)

Functions
---------

.. function:: wakeup(task, time_ms, repeat_ms = 0)

   This is a module factory function that returns an instance of the :py:class:`Timer` class.

Classes
-------

.. toctree::
    :maxdepth: 1

    wakeup.Timer.rst

