.. currentmodule:: datastore

:mod:`datastore` --- Data persistence services
==============================================

.. module:: datastore
   :synopsis: Data persistence services

.. admonition:: Coming soon
   :class: tip

   In this preview only data that has been saved in the factory data store is available for retrieval. For
   the workshop, we have populated the ImageStore with several splashscreen background images.

This module contains classes for managing storage and retrieval of application data. Persistent application
data is of two possible types:

   - *Factory settings:* Manufacturers can provision the DL-7450 with application data in the manufacturing 
     process, such as branded splashscreen backgrounds or the URL of a content provider. It
     is also possible to provide unique-per-dock (UPD) data, such as enrolment tokens for IoT cloud service
     providers.
   - *Runtime settings:* Applications may store data that is not set in the factory, but which persists across
     DL-7450 restarts. Such data may include access tokens for cloud providers or local network settings
     that have been provisioned remotely after the dock has been deployed in an enterprise setting.

There is an additional non-persistent storage type:

   - *Ephemeral settings:* Applications may store data that is useful at runtime, but is not essential to 
     store across dock restarts. For example, image data can be large, and it is not possible to keep many
     on the Python runtime memory heap. In this case an application can store them in out-of-process memory
     and retrieve them on demand. An example use-case is using the ephemeral storage area to avoid having
     to make slow HTTP requests to obtain subsequent data. 

There is an :py:class:`ImageStore` interface for retreiving images from the persistent data stores. The image
data is available as a python `bytearray` and the type is identified by one of the image type constants from the
:py:mod:`image` module. Alternatively, a token may be used for later retreiving an image. This may reduce the number
of copies of the image data created and used by your application.

Simple key-value pairs can be stored and retrieved using the :py:class:`KvStore` interface.


Constants
---------

.. data:: datastore.FACTORY_DATA
          datastore.APPLICATION_DATA

   Pick whether to use application data or factory data.

.. admonition:: Coming soon
   :class: tip

   These constants aren't available in this preview,
   and all data retrieval is from the factory data store.


Classes
-------

.. toctree::
    :maxdepth: 1

    datastore.ImageStore.rst


.. toctree::
    :maxdepth: 1

    datastore.KvStore.rst

