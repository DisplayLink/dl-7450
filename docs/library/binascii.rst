:mod:`binascii` -- binary/ASCII conversions
===========================================

.. module:: binascii
   :synopsis: binary/ASCII conversions

This module implements conversions between binary data and various
encodings of it in ASCII form (in both directions).

.. admonition:: Note
   :class: attention

   This is a limited implementation of :py:mod:`binascii` from the standard CPython
   implementation.


Functions
---------

.. function:: a2b_base64(data)

   Decode base64-encoded data, ignoring invalid characters in the input.
   Conforms to `RFC 2045 s.6.8 <https://tools.ietf.org/html/rfc2045#section-6.8>`_.
   Returns a `bytes` object.

.. function:: b2a_base64(data, *, newline=True)

   Encode binary data in base64 format, as in `RFC 3548
   <https://tools.ietf.org/html/rfc3548.html>`_. Returns the encoded data
   followed by a newline character if *newline* is true, as a `bytes` object.
