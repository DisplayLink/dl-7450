:mod:`hmac` -- hashing algorithms
====================================

.. module:: hmac
   :synopsis: hashing algorithms


Implements the standard Hash-based Message Authentication Code (HMAC) algorithm
from `RFC 2104 <https://datatracker.ietf.org/doc/html/rfc2104.html>`_. This
algorithm can be used to ensure that messages are from trusted sources, and also
that the message has not be tampered with in-transit. The algorithm requires a
hashing algorithm and a secret key. The :py:mod:`hashlib` module provides some
standard hash functions that can be used with this module. The following is an
example of how to use this module to create an authentication code for a
message. 

  :: 

    import binascii
    import hmac
    import hashlib
    from dock import DockInfo
    from splashscreen import Splashscreen
    from time import strftime

    HASH_KEY = b"myverysecretkey"
    DOCK_ID = DockInfo().dock_id()
    AUTH_KEY = "b446ad4b-887c-4b81-9db8-74e6834dba28"

    class AuthCode:
        def __init__(self, msg_id, msg):
            self.msg_id = msg_id
            self.msg = msg
            self.msg_time = strftime("%H:%M:%S (%Z)\n%d/%m/%Y")

        def code(self) -> str:
            msg_data = (str(self.msg_id) + self.msg + self.msg_time +
              DOCK_ID + AUTH_KEY)

            code = hmac.new(
                key=HASH_KEY,
                msg=binascii.b2a_base64(msg_data),
                digestmod=hashlib.md5)

            return code.hexdigest()

    screen = Splashscreen()
    msg_id = 42
    message = "Hello, world!"
    auth_code = AuthCode(msg_id, message)
    screen.add_text_box([
        f"Message {msg_id}: {message}",
        f"HMAC: {auth_code.code()}"
    ])

Functions
---------
.. function:: new(key, msg=None, digestmod=None)
   
   Return a new :py:class:`HMAC` object. The parameters are:

     - *key* is an object satisfying the buffer protocol, containing the secret key.
     - *msg* is an object satisfying the buffer protocol. The method
     - *digestmod* is a :py:mod:`hashlib` constructor returning a new hash object. 

   ::

    import hashlib
    import hmac
    from splashscreen import Splashscreen
      
    screen = Splashscreen()
    m = hmac.new(b"key", b"hello, world", hashlib.md5)
    screen.add_text_box(f"digest: {m.digest()}")
    
    # Displays:
    # digest: b'4LF\xd2O|\xcc\x1c\x99\x1clp@x\xe8\\'

Classes
-------

.. toctree::
    :maxdepth: 1

    hmac.HMAC.rst
