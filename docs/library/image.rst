.. currentmodule:: image

:mod:`image` --- representation of image types
==============================================

.. module:: image
   :synopsis: Representation of image types

This module contains constants defining representations of images.

Classes
-------

.. class:: ImageToken()

   An opaque token representing image data from the :py:class:`datastore.ImageStore`. 
   Objects of this class cannot be created directly, but only through the
   `ImageStore.get_token` method.


Constants
---------

.. data:: image.NONE
          image.PNG
          image.BMP

   The image format used by, for example, `Splashscreen.set_background`.

