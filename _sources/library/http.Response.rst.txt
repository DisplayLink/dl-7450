.. currentmodule:: http
.. _http.Response:

class Response -- details of a response to an HTTP request
==========================================================

The Response class represents a response from a server to an 
HTTP request.

Application developers should not create a `Response` object 
directly, but should receive a correctly formed one as the result
of an HTTP request, such as `http.get` or `http.post`.


Constructors
------------

.. class:: Response

   Creates an HTTP response object. You should not need to do this manually.

Methods
-------

.. method:: Response.status_code()

   The HTTP response code, e.g. 200 for a successful HTTP request.
   Value over 100 indicate that the request was made succesfully. If
   the request was not made successfully, e.g. due to a DNS failure, 
   the return code is between 1 and 99. These correspond to curl failure codes;
   please refer to the curl documentation on curlcodes
   `here <https://curl.se/libcurl/c/libcurl-errors.html>`_.

.. method:: Response.headers()

   The HTTP response headers as a Python dictionary. For every ``key: value`` header
   in the response there will be an entry in the dictionary where ``key=value``.

.. method:: Response.body()

   The raw HTTP response body as a `bytearray`. The HTTP content-type
   header indicates what the MIME media type of the body is, for example ``text/html``
   or ``application/json``. The application should determine the MIME media type and
   convert the `bytearray` to the desired format.

   For instance, to covert a given response.body() to a `str`::

      response_as_str = str(response.body(), 'utf-8')

   If that `str` contained a JSON dictionary, it could then be parsed as follows::

      import json
      response_as_json = json.loads(response_as_str)
