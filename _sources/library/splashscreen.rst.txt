.. currentmodule:: splashscreen

:mod:`splashscreen` --- functions for controlling the DL-7450 splash screen
===========================================================================

.. module:: splashscreen
    :synopsis: functions related to controlling the splash screen content

This module contains functions and classes for presenting
content on the DisplayLink DL-7450 splash screen.

Overview
--------

The splash screen module allows developers to display text on all
screens connected to the DL-7450 device. It is possible to set a
background on which to render this text.

To render a splash screen, the Python application must first call a
number of commands using a `Splashscreen` object::

    screen = Splashscreen()
    screen.set_background(background)
    for i in range(10):
        y = 192 + i * 64
        screen.add_text_box(
            "ATTENTION",
            {
                "x": 960, "y": y,
                "alignment": Alignment.MIDDLE
            }
        )

As long as Python code continues to run, the elements will not be
drawn on the screen. Only when Python code is no longer executing
will a render to the screen be triggered. This allows the developer
to assemble all necessary elements on the screen before they are
displayed. So in the above example, the text "ATTENTION" will only
be rendered after all 10 instances have been added to the screen.

Note that this precludes using Python's `time.sleep` function to
delay the rendering of new elements. Instead, the application should
use :py:mod:`wakeup` to schedule these events to occur at the right
time in the future, and allow the Python code to finish running.

This paradigm is detailed more fully in the
:ref:`programming paradigm <dl_7450_paradigm>` documentation; it is
the way in which all time-based events should be scheduled in the
DL-7450 SDK.

Classes
-------

.. toctree::
    :maxdepth: 1

    splashscreen.Splashscreen.rst

Constants
---------

.. data:: Alignment.LEFT
          Alignment.RIGHT
          Alignment.MIDDLE

    Text alignment used in `Splashscreen.add_text_box`.

