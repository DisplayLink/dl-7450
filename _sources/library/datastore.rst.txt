.. currentmodule:: datastore

:mod:`datastore` --- Data persistence services
==============================================

.. module:: datastore
   :synopsis: Data persistence services

This module contains classes for managing storage and retrieval of application
data. Logically, the DL-7450 :py:mod:`datastore` is a single entity, with
different partitions. There is an :py:class:`ImageStore` interface for
retreiving images from the persistent data store. The image data is available
as a python `bytearray` and the type is identified by one of the image type
constants from the :py:mod:`image` module. Alternatively, a token may be used
for later retreiving an image. This may reduce the number of copies of the
image data created and used by your application. Simple key-value pairs can be
stored and retrieved using the :py:class:`KvStore` interface. The python
application itself also resides in the datastore, but is not explicitly
accessible from the application. In later releases of the SDK, storage for
futher types, such as fonts will be provided.

Data may also be stored in different ways. Persistent application data is of
two possible types:

   - *Factory settings* or *Read-only memory (ROM)* storage. Manufacturers can
     provision the DL-7450 with application data in the manufacturing process,
     such as branded splashscreen backgrounds or the URL of a content provider.
     It is also possible to provide unique-per-dock (UPD) data, such as
     enrolment tokens for IoT cloud service providers.
   - *Runtime settings:* Applications may store data that is not set in the
     factory, but which persists across DL-7450 restarts. Such data may include
     access tokens for cloud providers or local network settings that have been
     provisioned remotely after the dock has been deployed in an enterprise
     setting.

There is an additional non-persistent storage type:

   - *Ephemeral settings:* Applications may store data that is useful at
     runtime, but is not essential to store across dock restarts. For example,
     image data can be large, and it is not possible to keep many on the Python
     runtime memory storage. In this case an application can store them in
     out-of-process memory and retrieve them on demand. An example use-case is
     using the ephemeral storage area to avoid having to make slow HTTP
     requests to obtain subsequent data. 

When an application requests an item from the datastore, unless explicitly
stated otherwise, there is an order of preference. For example if the
application requests a splashscreen background with image tag *default_img*,
first the ephemeral store will be checked, followed by the runtime store and
finally the ROM/factory store. 

The amounts available for different types of data is currently as follows.
There is no restriction on how data is distributed across the available
storage, i.e. an applicaiton developer can use it as they see fit for code,
images and key-value data.

   +--------------+----------------------------+
   | Data Storage | Available                  |
   +==============+============================+
   | Factory/ROM  | 13MB                       |
   +--------------+----------------------------+
   | Runtime      | 13MB                       |
   +--------------+----------------------------+
   | Ephemeral    | 128MB                      |
   +--------------+----------------------------+


.. admonition:: Not-yet implemented
   :class: tip

   In the present version of the DL-7450 SDK only the application ROM store is
   implemented. 



Application ROM Storage during development
------------------------------------------

The Application ROM storage area, also referred to as *Factory storage*
provides a mechanism to deploy a customer application and associated data in
the manufacturing process. This enables the customer's DL-7450 dock to run the
customer application on first boot after sale to the end user. The semantics of
the application ROM store is as suggested by the name, a read-only data store.
This supports a factory-reset operation on the dock. One usage pattern might be
for a customer to ship a dock with a basic application in factory storage,
which bootstraps another application that requires user-specific data in the
field. Another usage pattern is that the application ROM store contains version
N of the application, which can be updated to a later version which is stored
in the runtime store. Yet another case is that the factory application might
provide corporate imagery of the dock manufacturer, which can be overridden in
the field by corporate imagery of the end-user. In all cases, a a factory reset
will cause the application and its data to be restored to the state that it was
manufactured in. 

Therefore, the :py:mod:`datastore` APIs in the DL-7450 SDK do not allow the ROM store
area to be written to. While this is the required behaviour in a production
docking station, it is too restrictive for development. To support development,
DisplayLink has provided a REST API in our development cloud to populate the
factory store. The details are provided with the :githubSamples:`supporting
scripts </scripts/README.md>`. Note that the operation is atomic and
destructive - i.e. the application ROM store is replaced in a single operation.
This mechanism will not be available to docks in production.

Ephemeral application code during development
---------------------------------------------

To support development, DisplayLink provides a REST API to deploy new
application code immediately to the dock. This makes use of ephemeral data
storage. The details of how to use this API are given with the
:githubSamples:`supporting scripts </scripts/README.md>`. 


Classes
-------

.. toctree::
    :maxdepth: 1

    datastore.ImageStore.rst


.. toctree::
    :maxdepth: 1

    datastore.KvStore.rst

