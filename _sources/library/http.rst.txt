.. currentmodule:: http

:mod:`http` --- functions for accessing external web services
=============================================================

.. module:: http
   :synopsis: functions providing DisplayLink DL-7450 access to HTTP endpoints

This module provides functions for making HTTP requests to web endpoints.
Requests can be made either synchronously or asynchronously.

A synchronous request blocks the Python application until a response is received
or the request times out.
An asynchronous request, on the other hand, is initiated in the background and
immediately returns control to the application.
Once the response is received, a callback function is invoked to handle it.

A running Python application can initiate up to 16 concurrent HTTP requests.
Any attempt to create additional requests beyond this limit will fail immediately
with ``status_code`` 89, corresponding to ``CURLE_NO_CONNECTION_AVAILABLE``.

If a request is sent without any data, a ``Content-Length: 0`` header will be
automatically included.

It is the developer’s responsibility to ensure the validity of all arguments.
For instance, although sending a GET request with a body is not standard practice
and has undefined behavior, the `http.get()` function still accepts a ``data``
argument if needed for a specific use case.


Synchronous HTTP requests
-------------------------

These functions perform HTTP requests and return responses as instances of the
:py:class:`http.Response` class. The function will block until a response is
received or the request fails.

.. function:: get(url, headers=None, data=None, **kwargs)

   Sends an HTTP GET request to the given ``url``.

.. function:: post(url, headers=None, data=None, **kwargs)

   Sends an HTTP POST request to the given ``url``.

.. _synchronous-attributes:

Each function returns an :ref:`http.Response <http.Response>` object containing
the status and response.

The request parameters are as follows:

  - *url*: A string representing a well-formed URL (Uniform Resource Locator).
  - *headers*: A `dict` of key-value pairs to be included in the request header
    as ``key: value``. Both keys and values must be strings.
  - *data*: A `bytes`-like object representing the body of the request.
  - *\*\*kwargs*: A set of optional keyword arguments passed to the request.

**Currently supported optional arguments:**
  - *timeout*: The number of seconds before the request times out. The default
    is 40. Setting this to 0 disables the timeout (use with caution, especially
    for synchronous requests).

  - *cacert*: A string containing one or more server certificates in X.509 format.
    If multiple certificates are provided, they should be concatenated in sequence
    within the string. By default, the system's CA certificate store is used to
    verify server authenticity. If *cacert* is specified, it overrides the system
    store and only the provided certificates are used for verification

    ::

      import http
      import json
      from splashscreen import Splashscreen

      URL = "https://6pantherpublicanonymous.blob.core.windows.net/dl-7450/content.json"
      CERTIFICATE = """
      -----BEGIN CERTIFICATE-----
      MIIOkTCCDHmgAwIBAgITMwGFNsXF9GOnABFWcQAAAYU2xTANBgkqhkiG9w0BAQwF
      ADBdMQswCQYDVQQGEwJVUzEeMBwGA1UEChMVTWljcm9zb2Z0IENvcnBvcmF0aW9u
      MS4wLAYDVQQDEyVNaWNyb3NvZnQgQXp1cmUgUlNBIFRMUyBJc3N1aW5nIENBIDAz
      MB4XDTI1MDEyMDExMDQyMVoXDTI1MDcxOTExMDQyMVowbjELMAkGA1UEBhMCVVMx
      CzAJBgNVBAgTAldBMRAwDgYDVQQHEwdSZWRtb25kMR4wHAYDVQQKExVNaWNyb3Nv
      ZnQgQ29ycG9yYXRpb24xIDAeBgNVBAMMFyouYmxvYi5jb3JlLndpbmRvd3MubmV0
      MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy6OaDfkcZ1YAcXut8oGq
      XRqGDlvWT/7vL6u3kJUOP2Dx5PlA7TaC/TF3UURTgv/vIjYUkOp0J+JfS0OTB9Df
      yqGIObl0YNffXFxrK+J7Wj59fVm/yH+LhgB04NsQYKoLl0sq/sbn9sd1pxtj/Y59
      xdpU+svPnCUEwGFy8VMctMu3+gIV/8z49unxq4YrRye4MQ09sF7b0NqvItXQfnPG
      WykmBdWO31oTmySR/KwRcouozDflJ2/JLr0AO/BbK3IHG2dfSspuIbidz+U2b8Qg
      cqZR0WaoOZEtPWI3M2ZeLPfR0mEOI75HsHuhcMhivkj97HvbfNp2u+zaLcW9f211
      2QIDAQABo4IKNzCCCjMwggGABgorBgEEAdZ5AgQCBIIBcASCAWwBagB2AN3cyjSV
      1+EWBeeVMvrHn/g9HFDf2wA6FBJ2Ciysu8gqAAABlINrwRUAAAQDAEcwRQIhAMBh
      c9Oda2/jXqiQ7TYhxq8p6PPgUj+Vpl9kGGPcuaobAiBmHUkWTXFjBq+cg7TL8FG4
      6RNKHcm5Pm6kiNcfi+h5nwB3AH1ZHhLheCp7HGFnfF79+NCHXBSgTpWeuQMv2Q6M
      Lnm4AAABlINrwMUAAAQDAEgwRgIhAKzBU0EkR87P4N28ynMktrVwmu784bOewF0U
      8oK9ERYSAiEAgWk8Lrwp6U/tTDibLaNOtlxk8B73uK/dU/y+pCg4ZE0AdwAaBP9J
      0FQdQK/2oMO/8djEZy9O7O4jQGiYaxdALtyJfQAAAZSDa8FSAAAEAwBIMEYCIQDX
      OHoOZQm/1drHta3XJia/y7UUP8jr6nHnhfPnIET4bwIhAMO5dAbFvLHGU5n201Sf
      RnD242lafoXW/TAKa/h6eRjVMCcGCSsGAQQBgjcVCgQaMBgwCgYIKwYBBQUHAwIw
      CgYIKwYBBQUHAwEwPAYJKwYBBAGCNxUHBC8wLQYlKwYBBAGCNxUIh73XG4Hn60aC
      gZ0ujtAMh/DaHV2Cq+cwh+3xHwIBZAIBLTCBtAYIKwYBBQUHAQEEgacwgaQwcwYI
      KwYBBQUHMAKGZ2h0dHA6Ly93d3cubWljcm9zb2Z0LmNvbS9wa2lvcHMvY2VydHMv
      TWljcm9zb2Z0JTIwQXp1cmUlMjBSU0ElMjBUTFMlMjBJc3N1aW5nJTIwQ0ElMjAw
      MyUyMC0lMjB4c2lnbi5jcnQwLQYIKwYBBQUHMAGGIWh0dHA6Ly9vbmVvY3NwLm1p
      Y3Jvc29mdC5jb20vb2NzcDAdBgNVHQ4EFgQUYTyeDm+nd5eMItYwKc7WIwAOwJ8w
      DgYDVR0PAQH/BAQDAgWgMIIGPAYDVR0RBIIGMzCCBi+CFyouYmxvYi5jb3JlLndp
      bmRvd3MubmV0gicqLmxvbjI0cHJkc3RyMTBhLnN0b3JlLmNvcmUud2luZG93cy5u
      ZXSCGCouYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIbKi56MS5ibG9iLnN0b3JhZ2Uu
      YXp1cmUubmV0ghsqLnoyLmJsb2Iuc3RvcmFnZS5henVyZS5uZXSCGyouejMuYmxv
      Yi5zdG9yYWdlLmF6dXJlLm5ldIIbKi56NC5ibG9iLnN0b3JhZ2UuYXp1cmUubmV0
      ghsqLno1LmJsb2Iuc3RvcmFnZS5henVyZS5uZXSCGyouejYuYmxvYi5zdG9yYWdl
      LmF6dXJlLm5ldIIbKi56Ny5ibG9iLnN0b3JhZ2UuYXp1cmUubmV0ghsqLno4LmJs
      b2Iuc3RvcmFnZS5henVyZS5uZXSCGyouejkuYmxvYi5zdG9yYWdlLmF6dXJlLm5l
      dIIcKi56MTAuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MTEuYmxvYi5zdG9y
      YWdlLmF6dXJlLm5ldIIcKi56MTIuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56
      MTMuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MTQuYmxvYi5zdG9yYWdlLmF6
      dXJlLm5ldIIcKi56MTUuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MTYuYmxv
      Yi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MTcuYmxvYi5zdG9yYWdlLmF6dXJlLm5l
      dIIcKi56MTguYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MTkuYmxvYi5zdG9y
      YWdlLmF6dXJlLm5ldIIcKi56MjAuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56
      MjEuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MjIuYmxvYi5zdG9yYWdlLmF6
      dXJlLm5ldIIcKi56MjMuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MjQuYmxv
      Yi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MjUuYmxvYi5zdG9yYWdlLmF6dXJlLm5l
      dIIcKi56MjYuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MjcuYmxvYi5zdG9y
      YWdlLmF6dXJlLm5ldIIcKi56MjguYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56
      MjkuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MzAuYmxvYi5zdG9yYWdlLmF6
      dXJlLm5ldIIcKi56MzEuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MzIuYmxv
      Yi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MzMuYmxvYi5zdG9yYWdlLmF6dXJlLm5l
      dIIcKi56MzQuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MzUuYmxvYi5zdG9y
      YWdlLmF6dXJlLm5ldIIcKi56MzYuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56
      MzcuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56MzguYmxvYi5zdG9yYWdlLmF6
      dXJlLm5ldIIcKi56MzkuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56NDAuYmxv
      Yi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56NDEuYmxvYi5zdG9yYWdlLmF6dXJlLm5l
      dIIcKi56NDIuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56NDMuYmxvYi5zdG9y
      YWdlLmF6dXJlLm5ldIIcKi56NDQuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56
      NDUuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56NDYuYmxvYi5zdG9yYWdlLmF6
      dXJlLm5ldIIcKi56NDcuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56NDguYmxv
      Yi5zdG9yYWdlLmF6dXJlLm5ldIIcKi56NDkuYmxvYi5zdG9yYWdlLmF6dXJlLm5l
      dIIcKi56NTAuYmxvYi5zdG9yYWdlLmF6dXJlLm5ldDAMBgNVHRMBAf8EAjAAMGoG
      A1UdHwRjMGEwX6BdoFuGWWh0dHA6Ly93d3cubWljcm9zb2Z0LmNvbS9wa2lvcHMv
      Y3JsL01pY3Jvc29mdCUyMEF6dXJlJTIwUlNBJTIwVExTJTIwSXNzdWluZyUyMENB
      JTIwMDMuY3JsMGYGA1UdIARfMF0wUQYMKwYBBAGCN0yDfQEBMEEwPwYIKwYBBQUH
      AgEWM2h0dHA6Ly93d3cubWljcm9zb2Z0LmNvbS9wa2lvcHMvRG9jcy9SZXBvc2l0
      b3J5Lmh0bTAIBgZngQwBAgIwHwYDVR0jBBgwFoAU/glxQFUFEETYpIF1uJ4a6UoG
      iMgwHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMBMA0GCSqGSIb3DQEBDAUA
      A4ICAQBCJFYJ3SWuIrsxQjneg+MxaON8LJHByW1OS1lzAFMcHRNAzdBkxTyOezKz
      xtFTlQATr8JaaEbMuvlONBASB0NKJ9PdVu4WIhLyr/Tk2Y9aHAnbY5Dpk/QUF37K
      qOmDQpGMlbjFd7SKEkTfbxqJhfcstis8ixFNQRIvYrVWQEjyBYJN0rcI0Esg3qik
      SXpIsnngiIZrERJBGNjR5N/DbeJn0JH5iQm+mTTHOLXfgzQSsKm7TWMVJNHoIxeF
      bk8j9EN0iSVP+RtKzd0oyizG5Q0JkjFo0beVLZuGTNGeQJLIEagP/7p6Unoq61xV
      itILjfsZ5reh4CbbySMg9mEjq+v887xvYMRmtqdJWInRqEwW5kakfK+PImz5SinZ
      xpbSwPAxjz1sHKZ3ad9QOWV62PtJh9rgGSDQcOSdEKqbl2m+BNn4F7RTuAMQVrv7
      RAJged+QsrGfPN+wNmpT9NpNkFHZvkphGW3EBfWlSulGUylyyxOM8okoFGyOAt/X
      yn2GfIkI6WW8cM/nMrUHi/b9jwLw40DfZF8/flAZ/isxndOXnJhaAIduSKVjCCwb
      389Vj2D3EnhM41jWO5znhX07pfYXG4qVxLgJVkqeaGRh1KV+EYLXxJjYbPA30HQA
      wY4ADBLKxWlyQ/R8vgX7p3z26+FWxFQ4Vg13cQk8toiO1kw4kA==
      -----END CERTIFICATE-----
      """

      screen = Splashscreen()

      response = http.get(URL, cacert=CERTIFICATE)
      if response.status_code() != 200:
          screen.add_text_box(f"error: {response.status_code()}")
      else:
          content = json.loads(response.body())
          items = content["data"]["images"]
          screen.add_text_box(items)

   The certificate can be stored as a string in the
   :py:class:`datastore.KvStore`, such as::

      import http
      from splashscreen import Splashscreen
      from datastore import KvStore

      URL = "https://6pantherpublicanonymous.blob.core.windows.net/dl-7450/content.json"
      CERTIFICATE = KvStore().get("cacert")

      screen = Splashscreen()

      def cb(response):
        if response.status_code() != 200:
          screen.add_text_box(
            f"error: {response.status_code()}")
        else:
          screen.add_text_box("Got content")

      http.get_async(URL, cb, cacert=CERTIFICATE)



Asynchronous HTTP requests
--------------------------

These functions initiate HTTP requests asynchronously. The provided callback
function handles the response.

.. function:: get_async(url, on_response, headers=None, data=None, **kwargs)

   Sends an HTTP GET request to the given ``url`` without blocking program flow.

.. function:: post_async(url, on_response, headers=None, data=None, **kwargs)

   Sends an HTTP POST request to the given ``url`` without blocking program flow.

The parameters are the same as their :ref:`synchronous counterparts <synchronous-attributes>`,
with the addition of:

  - *on_response*: A Python callable that takes a single parameter. When the
    request is complete, the *on_response* function is called with the resulting
    :ref:`http.Response <http.Response>` as its argument.

Example:::

   import http
   import json
   from wakeup import wakeup
   from splashscreen import Splashscreen

   url = "https://6pantherpublicanonymous.blob.core.windows.net/dl-7450/content2.json"

   splashscreen = Splashscreen()

   def on_response(response):
       if response.status_code() != 200:
           raise Exception("Error getting content")
       content = json.loads(response.body())
       items = content["data"]["images"]
       splashscreen.add_text_box(items)

   http.get_async(url, on_response, timeout=20)



Classes
-------

.. toctree::
    :maxdepth: 1

    http.Response.rst
