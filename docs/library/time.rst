:mod:`time` -- time related functions
=====================================

.. module:: time
   :synopsis: time related functions

The ``time`` module provides functions for getting the current time and date,
measuring time intervals, and for delays.

This verison of Python uses the standard POSIX systems epoch of
1970-01-01 00:00:00 UTC.

The DL-7450 uses the Network Time Protocol (NTP) to set the system time.


Functions
---------

.. function:: gmtime([secs])
              localtime([secs])

   Convert the time *secs* expressed in seconds since the Epoch (see above) into an
   8-tuple which contains: ``(year, month, mday, hour, minute, second, weekday, yearday)``
   If *secs* is not provided or None, then the current time from the RTC is used.

   The `gmtime()` function returns a date-time tuple in UTC, and `localtime()` returns a
   date-time tuple in local time.

   The format of the entries in the 8-tuple are:

   * year includes the century (for example 2014).
   * month   is 1-12
   * mday    is 1-31
   * hour    is 0-23
   * minute  is 0-59
   * second  is 0-59
   * weekday is 0-6 for Mon-Sun
   * yearday is 1-366

.. function:: mktime()

   This is inverse function of localtime. It's argument is a full 8-tuple
   which expresses a time as per localtime. It returns an integer which is
   the number of seconds since Jan 1, 2000.

.. function:: sleep(seconds)

   Sleep for the given number of *seconds*. *seconds* may be a floating-point
   number; this will result in the DL-7450 sleeping for a fractional number of
   seconds.

.. function:: sleep_ms(ms)

   Delay for given number of milliseconds, should be positive or 0.

   This function will delay for at least the given number of milliseconds, but
   may take longer than that if other processing must take place, for example
   interrupt handlers or other threads.  Passing in 0 for *ms* will still allow
   other processing to occur.  Use `sleep_us()` for more precise delays.

.. function:: sleep_us(us)

   Delay for given number of microseconds, should be positive or 0.

   This function attempts to provide an accurate delay of at least *us*
   microseconds, but it may take longer if the system has other higher priority
   processing to perform.

.. function:: ticks_ms()

    Returns an increasing millisecond counter with an arbitrary reference point, that
    wraps around after some value.

    The wrap-around value is not explicitly exposed, but we will
    refer to it as *TICKS_MAX* to simplify discussion. Period of the values is
    *TICKS_PERIOD = TICKS_MAX + 1*. *TICKS_PERIOD* is guaranteed to be a power of
    two, but otherwise may differ from port to port. The same period value is used
    for all of `ticks_ms()`, `ticks_us()`, `ticks_cpu()` functions (for
    simplicity). Thus, these functions will return a value in range [*0* ..
    *TICKS_MAX*], inclusive, total *TICKS_PERIOD* values. Note that only
    non-negative values are used. For the most part, you should treat values returned
    by these functions as opaque. The only operations available for them are
    `ticks_diff()` and `ticks_add()` functions described below.

    Note: Performing standard mathematical operations (+, -) or relational
    operators (<, <=, >, >=) directly on these value will lead to invalid
    result. Performing mathematical operations and then passing their results
    as arguments to `ticks_diff()` or `ticks_add()` will also lead to
    invalid results from the latter functions.

.. function:: ticks_us()

   Just like `ticks_ms()` above, but in microseconds.

.. function:: ticks_cpu()

   Similar to `ticks_ms()` and `ticks_us()`, but with the highest possible resolution
   in the system. This function is intended for very fine benchmarking or very tight
   real-time loops.


.. function:: ticks_add(ticks, delta)

   Offset *ticks* by a given number, which can be either positive or negative.
   Given a *ticks* value, this function allows to calculate a ticks value *delta*
   ticks before or after it, following modular-arithmetic definition of tick values
   (see `ticks_ms()` above). *ticks* parameter must be a direct result of call
   to `ticks_ms()`, `ticks_us()`, or `ticks_cpu()` functions (or from previous
   call to `ticks_add()`). However, *delta* can be an arbitrary integer number
   or numeric expression. `ticks_add()` is useful for calculating deadlines for
   events/tasks. (Note: you must use `ticks_diff()` function to work with
   deadlines.)

   Examples::

        # Find out what ticks value there was 100ms ago
        print(ticks_add(time.ticks_ms(), -100))

        # Calculate deadline for operation and test for it
        deadline = ticks_add(time.ticks_ms(), 200)
        while ticks_diff(deadline, time.ticks_ms()) > 0:
            do_a_little_of_something()

        # Find out TICKS_MAX used by this port
        print(ticks_add(0, -1))


.. function:: ticks_diff(ticks1, ticks2)

   Measure ticks difference between values returned from `ticks_ms()`, `ticks_us()`,
   or `ticks_cpu()` functions, as a signed value which may wrap around.

   The argument order is the same as for subtraction
   operator, ``ticks_diff(ticks1, ticks2)`` has the same meaning as ``ticks1 - ticks2``.
   However, values returned by `ticks_ms()`, etc. functions may wrap around, so
   directly using subtraction on them will produce incorrect result. That is why
   `ticks_diff()` is needed, it implements modular (or more specifically, ring)
   arithmetic to produce correct result even for wrap-around values (as long as they not
   too distant in between, see below). The function returns a **signed** value in the range
   [*-TICKS_PERIOD/2* .. *TICKS_PERIOD/2-1*] (that's a typical range definition for
   two's-complement signed binary integers). If the result is negative, it means that
   *ticks1* occurred earlier in time than *ticks2*. Otherwise, it means that
   *ticks1* occurred after *ticks2*. This holds **only** if *ticks1* and *ticks2*
   are apart from each other for no more than *TICKS_PERIOD/2-1* ticks. If that does
   not hold, incorrect result will be returned. Specifically, if two tick values are
   apart for *TICKS_PERIOD/2-1* ticks, that value will be returned by the function.
   However, if *TICKS_PERIOD/2* of real-time ticks has passed between them, the
   function will return *-TICKS_PERIOD/2* instead, i.e. result value will wrap around
   to the negative range of possible values.

   `ticks_diff()` is designed to accommodate various usage patterns, among them:

   * Polling with timeout. In this case, the order of events is known, and you will deal
     only with positive results of `ticks_diff()`::

        # Wait for GPIO pin to be asserted, but at most 500us
        start = time.ticks_us()
        while pin.value() == 0:
            if time.ticks_diff(time.ticks_us(), start) > 500:
                raise TimeoutError

   * Scheduling events. In this case, `ticks_diff()` result may be negative
     if an event is overdue::

        # This code snippet is not optimized
        now = time.ticks_ms()
        scheduled_time = task.scheduled_time()
        if ticks_diff(scheduled_time, now) > 0:
            print("Too early, let's nap")
            sleep_ms(ticks_diff(scheduled_time, now))
            task.run()
        elif ticks_diff(scheduled_time, now) == 0:
            print("Right at time!")
            task.run()
        elif ticks_diff(scheduled_time, now) < 0:
            print("Oops, running late, tell task to run faster!")
            task.run(run_faster=true)

   Note: Do not pass `time()` values to `ticks_diff()`, you should use
   normal mathematical operations on them. But note that `time()` may (and will)
   also overflow. This is known as https://en.wikipedia.org/wiki/Year_2038_problem.


.. function:: time()

   Returns the number of seconds, as an integer, since the Epoch.

   .. admonition:: Difference to CPython
      :class: attention

      In CPython, this function returns the number of seconds since Unix epoch,
      1970-01-01 00:00 UTC, as a floating-point.

.. function:: time_ns()

    Similar to `time()` but returns nanoseconds since the Epoch, as an integer.

.. function:: strftime(fmt_string, [time_tuple])

    Create a readable string from the time. The *fmt_string* is compatible with the `C Python
    strfmt function <https://docs.python.org/3/library/time.html#time.strftime>`_. The second
    parameter is a time-tuple, as returned by `time.localtime` or `time.gmtime`. If this parameter
    is omitted, then the current time is used.
