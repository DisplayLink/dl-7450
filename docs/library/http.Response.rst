.. currentmodule:: http
.. _http.Response:

class Response -- details of a response to an HTTP request
==========================================================

The Response class represents a server's response to an HTTP request.

Application developers should not create a `Response` object
directly, but should receive a correctly formed one as the result
of an HTTP request method, such as `http.get` or `http.post`.


.. class:: Response

   Represents an HTTP response object. You typically do not need to
   instantiate this manually.

  .. method:: Response.status_code()

    Returns the HTTP status code, e.g., 200 for a successful request.
    Values above 100 indicate that the request was completed and a response
    was received. If the request could not be made successfully (e.g., due
    to a DNS failure), the return code will be between 1 and 99. These
    correspond to cURL failure codes; please refer to the cURL documentation
    on error codes `here <https://curl.se/libcurl/c/libcurl-errors.html>`_.

  .. method:: Response.headers()

    Returns the HTTP response headers as a Python dictionary. Each ``key: value``
    pair from the response is available in the dictionary as ``key = value``.

  .. method:: Response.body()

    Returns the raw HTTP response body as a `bytearray`. The content-type HTTP
    header indicates the MIME media type of the body, such as ``text/html`` or
    ``application/json``. The application should inspect this header to determine
    how to decode the body.

    For instance, to convert a given response.body() to a `str`::

       response_as_str = str(response.body(), 'utf-8')

    If that `str` contains a JSON dictionary, it can be parsed like this::

       import json
       response_as_json = json.loads(response_as_str)
