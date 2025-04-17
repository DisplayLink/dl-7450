:mod:`hashlib` -- hashing algorithms
====================================

.. module:: hashlib
   :synopsis: hashing algorithms

This module is a partial implementation of the corresponding CPython hashlib
module, and contains some common binary data hashing algorithms. This module is
part of the MicroPython core library.

* SHA256 - The current generation, modern hashing algorithm (of SHA2 series).
  It is suitable for cryptographically-secure purposes.

* SHA1 - A previous generation algorithm. Not recommended for new usages.

* MD5 - A legacy algorithm, not considered cryptographically secure.

Constructors
------------

In all of the following, ``data`` is any object that satisfies the buffer
protocol, including string, byte, bytearray or memoryview objects.

.. class:: hashlib.sha256([data])

    Create an SHA256 hasher object and optionally feed ``data`` into it.

.. class:: hashlib.sha1([data])

    Create an SHA1 hasher object and optionally feed ``data`` into it.

.. class:: hashlib.md5([data])

    Create an MD5 hasher object and optionally feed ``data`` into it.

    ::

      import hashlib
      from splashscreen import Splashscreen
      
      screen = Splashscreen()
      hash = hashlib.md5(b"hello, world")
      screen.add_text_box(f"digest: {hash.digest()}")

      # displays:
      # digest: b'\xe4\xd7\xf1\xb4\xed.B\xd1X\x98\xf4\xb2{\x01\x9d\xa4'

Methods
-------

In all of the following, ``data`` is any object that satisfies the buffer
protocol, including string, byte, bytearray or memoryview objects.

.. method:: hash.update(data)

   Feed more binary data into hash.

    ::

      import hashlib
      from splashscreen import Splashscreen
      
      screen = Splashscreen()
      hash = hashlib.md5(b"hello")
      hash.update(b", world")
      screen.add_text_box(f"digest: {hash.digest()}")

      # displays:
      # digest: b'\xe4\xd7\xf1\xb4\xed.B\xd1X\x98\xf4\xb2{\x01\x9d\xa4'

.. method:: hash.digest()

   Return hash for all data passed through hash, as a bytes object. After this
   method is called, no more data be fed into the hash.

    ::

      import hashlib
      
      hash = hashlib.md5(b"hello")
      digest = hash.digest()

      # either of the following calls results in an error
      # hash.update(b", world")
      # hash.digest()

.. method:: hash.hexdigest()

   This method is NOT implemented. Use ``binascii.hexlify(hash.digest())``
   to achieve a similar effect.


    ::

      import hashlib
      from binascii import hexlify
      from splashscreen import Splashscreen
      
      screen = Splashscreen()
      hash = hashlib.md5(b"hello, world")
      
      # The following line results in an error
      # screen.add_text_box(f"hexdigest: {hash.hexdigest()}")

      # Use this instead:
      screen.add_text_box(f"hexdigest: {hexlify(hash.digest())}")

      # displays
      # hexdigest: b'e4d7f1b4ed2e42d15898f4b27b019da4'
