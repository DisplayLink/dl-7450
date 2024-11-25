.. currentmodule:: splashscreen
.. _splashscreen.Splashscreen:

class Splashscreen -- control the DL-7450 splashscreen
======================================================

The *Splashscreeen* class enables control of the DL-7450 splashscreen.  

For example::

    from splashscreen import Splashscreen 
    from datastore import ImageStore

    images = ImageStore()
    background = images.get_token("default")

    screen = Splashscreen()
    screen.set_background(background)
    screen.add_text_box([
     "<span size=\"large\">Info: <b>Company Anniversary Celebration</b>",
     "Today @ 10:00am in the Atrium</span>"
    ])

Constructors
------------

.. class:: Splashscreen()

   Construct an object for controlling the DL-7450 splashscreen.

Methods
-------

.. method:: Splashscreen.set_background(background, image_type = image.PNG)

   Set the screen background. The parameters are:

      - *background* is either a `bytearray` object or an `ImageToken` obtained from `ImageStore.get_token`.
        The latter is an optimisation to delay multiple copying of the image from flash storage until it
        needed by the splashscreen renderer.
      - *image_type* is a constant defined in the :py:mod:`image` module describing the format of the image.


.. admonition:: Coming soon
   :class: tip

   In this preview only `image.PNG` is supported. The data must represent a 
   1920x1080 image. The background images stored in the factory data store for
   the workshop are in the correct format, as are those that are retreived from
   the network for the carousel sample. In the first release of the SDK these 
   restrictions will be removed and other formats such as BMP or JPG will be 
   allowed. The SDK will also allow different sized background images to be used
   and either centred or scaled on the screen. The interface will also allow different
   screen resolutions to be set.


.. method:: Splashscreen.add_text_box(text, attributes)

   Place text on the screen. The parameters are:

      - *text* is either a string or a list of strings. In the case of a list, each
        entry is interpreted as a new line. At present the string can be plain text or
        markup in `Pango markup <https://docs.gtk.org/Pango/pango_markup.html>`_.
      - *attributes* is an optional dictionary describing the position and alignment
        of the text. Possible key-value entries for this dictionary are:

        * *x*, *y* - coordinates to place the text at.
        * *alignment* - an :py:obj:`Alignment` constant from :py:mod:`splashscreen` specifying the text alignment.

        If this paramater is omitted, the text box is placed in the default user message
        area, in the centre of the screen.
   
   The text box is identified by its ``(x, y)`` position. Adding a second
   text box at the same coordinates has the effect of updating the text box. A text box
   can be removed by `Splashscreen.remove_text_box`.


.. method:: Splashscreen.remove_text_box(x, y)

   Remove a text box that was previously placed on the splashscreen at the given coordinates.
