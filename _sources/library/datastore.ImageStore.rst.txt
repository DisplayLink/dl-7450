.. currentmodule:: datastore
.. _datastore.ImageStore:

class ImageStore -- store and retrieve image data
=================================================


Constructors
------------

.. class:: ImageStore()

   Construct an ImageStore object.

Methods
-------

.. method:: ImageStore.list()

   List the tags of all available images.

.. method:: ImageStore.get(image_tag)

   Retrieve an image from its tag. The return value is a tuple ``(image_data, image_type)``, where:

    * *image_data* is a `bytearray` containing the raw pixel values of the image.
    * *image_type* is a constant from :py:mod:`image` specifying the image format.

.. method:: ImageStore.get_token(image_tag)

   Returns an opaque `image.ImageToken` that can be passed to :py:class:`splashscreen.Splashscreen` methods. Unlike the 
   previous method, this call does not result in the copying of the image from flash storage into
   a python bytearray. The token can be passed instead. This may result in faster rendering of the
   splash screen background. 

