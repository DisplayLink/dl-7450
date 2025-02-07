.. _dl_7450_paradigm:

Programming paradigm
====================

When executing code on the DL-7450, the application runs using a
single thread of execution. Whilst this thread (henceforth called
the Python thread) executes, there are a number of actions that
cannot be performed:

  * The execution of any callbacks, whether they are timers set via
    :func:`wakeup`, responses from async :py:mod:`http` requests or
    responses to changes in the state of DL-7450 hardware (e.g.
    :py:mod:`gpio` pins).
  * The rendering of elements added, removed or modified on the
    :py:mod:`splashscreen`.

The use of `time.sleep` therefore is *highly* discouraged, as it
will prevent any of these core SDK functionalities from occuring.

Instead, application developers are encouraged to write applications
that react to events, using the main component of the app mostly to
set up :py:class:`wakeup.Timer`\ s and other callbacks.

Once the Python thread finishes processing the Python code, it is
now able to go idle and allow timers, callbacks and rendering to
occur.

The use of dedicated callbacks where available is also highly
encouraged over proactively polling state using a
:py:class:`wakeup.Timer`; this will result in much more responsive
applications.
