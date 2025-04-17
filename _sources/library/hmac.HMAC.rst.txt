.. currentmodule:: hmac
.. _hmac.HMAC:

class HMAC -- Keyed Hashing for Message Authentication
======================================================

Objects of the HMAC class have the following methods

.. class:: HMAC(key, msg=None, digestmod=None)

   Create an HMAC object. Equivalent to and called by `hmac.new`.

  .. method:: copy()
    
    Returns a copy of this HMAC object. The original and the copy can be updated
    independently.

    .. admonition:: Note

      Not implemented for :py:mod:`hashlib` built-in hash functions

  .. method:: update(msg)
   
    Feed more data from the message into this object::

      import hashlib
      import hmac
      from splashscreen import Splashscreen
      
      screen = Splashscreen()
      m = hmac.new(b"key", b"hello", hashlib.md5)
      m.update(b", world")
      screen.add_text_box(f"digest: {m.digest()}")
    
      # Displays:
      # digest: b'4LF\xd2O|\xcc\x1c\x99\x1clp@x\xe8\\'

  .. method:: digest()

    Return the hash value of this hashing object. Returns the hmac value as
    bytes. If the underlying hash function's ``digest`` method is final, then
    this method is also final. 

  .. method:: hexdigest()

    Like `digest`, but returns a string of hexadecimal digits instead.

    ::

      import hashlib
      import hmac
      from splashscreen import Splashscreen
      
      screen = Splashscreen()
      m = hmac.new(b"key", b"hello, world", hashlib.md5)
      screen.add_text_box(f"hexdigest: {m.hexdigest()}")
    
      # Displays:
      # hexdigest: 344c46d24f7ccc1c991c6c704078e85c      

  .. property:: block_size
    
    The internal block size of the underlying hash algorithm in bytes. 

  .. property:: digest_size
  
    The size of the resulting digest in bytes; only supported if the underlying
    hash function has the ``digest_size`` attribute.
