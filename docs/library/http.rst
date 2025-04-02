.. currentmodule:: http

:mod:`http` --- functions for accessing external web services
=============================================================

.. module:: http
   :synopsis: functions giving DisplayLink DL-7450 web access

This module contains functions for accessing HTTP endpoints on the web, allowing
application developers to create a wide variety of features for end users. In 
simple cases the DL-7450 could fetch splash screen content from content provider
hosted in the cloud or within a corporate network.


Synchronous HTTP requests
-------------------------

These functions perform an HTTP request and return the response.

.. function:: get(url, headers=None, data=None)

   Send an HTTP GET request to the given ``url``.

.. function:: post(url, headers=None, data=None)

   Send an HTTP POST request to the given ``url``.


.. _synchronous-attributes:

For all these request functions:

 * A `dict` of key-value pairs can be specified for the ``headers``. These will
   each be listed as ``key: value`` in the HTTP request header.
 * Any `bytes`-like data specified in ``data`` will constitute the body of the
   request.
 * They all return an :ref:`http.Response <http.Response>` object populated
   with the result and response of the request.

Program flow will pause until a response is received from the server, or the
request fails.

A maximum of 16 HTTP requests can be made by a running Python app. Attempting to
create further requests will cause the request to immediately fail with
``status_code`` 89, corresponding to ``CURLE_NO_CONNECTION_AVAILABLE``.

If a request is sent without any data, a ``Content-Length: 0`` header will
automatically be included with the request.

It is up to the user to ensure that all specified arguments are valid. For
instance, sending a GET request with a body has undefined semantics, but the
user may still provide ``data`` for an `http.get()` call if it suits their
use case.


Asynchronous HTTP requests
--------------------------

These functions perform an HTTP request and return the response.

.. function:: get_async(url, on_complete, headers=None, data=None)

   Send an HTTP GET request to the given ``url`` without blocking program
   flow.

.. function:: post_async(url, on_complete, headers=None, data=None)

   Send an HTTP POST request to the given ``url`` without blocking program
   flow.

`These functions have all the same attributes as their synchronous counterparts
<synchronous-attributes>`, but:

 * An additional ``on_complete`` parameter must be specified. This must be a
   Python callable that takes one parameter.
 * Upon the completion of the request, the ``on_complete`` function will be
   called, with the :ref:`http.Response <http.Response>` that would have
   been returned from the corresponding synchronous function as its only
   argument.
 * These functions will return a control object that will allow the user to
   cancel the request, instead of an :ref:`http.Response <http.Response>`
   object.


Classes
-------

.. toctree::
    :maxdepth: 1

    http.Response.rst
