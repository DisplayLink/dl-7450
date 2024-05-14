

When you receive your evaluation DL-7450 board, you will also receive some
pieces of information that are required to deploy code to the board using the
DisplayLink development server. Your account is identified by the following tokens
 * `ENTERPRISE-ID`. This is a token to identify the entity that owns the
   DL-7450. It is unique to your organisation, and serves to ensure that code
   can only be deployed to docks that you own.
 * `APPLICATION-KEY` and `APPLICATION-SECRET`. You can think of these as a
   username and password. They are secrets that are used as authentication
   tokens. They will be provided to you securely via the usual mechanisms for
   distributing DisplayLink artefacts to customers. Please treat these tokens
   as secret and do not distribute to anyone who is not authorised to deploy
   code to the DL-7450 evaluation board.

In addition, you will be provided with a dock identifier, that looks like
```
DOCK-ID = "BC385DB79E2B94DC70E44422FCFFB29C0D90FCA7F024AC72625D7376233CFC02"
```

With these four pieces of information, the [send_code.py] script can be used for deploying code to the board:

```
python3 ./send_code.py -k <APPLICATION-KEY> -s <APPLICATION-SECRET> -e <ENTERPRISE-ID> -d <DOCK-ID> -f myapplication.py
```

You are free to design your own mechanism to deploy the code, based on this
script. For completeness we provide a description of the deployment process.
Code is sent to a DL-7450 by making an HTTP POST request to a REST endpoint in
the DisplayLink development server, located at
`https://sandbox.vision.synaptics.com`. There are two steps.

First, obtain an _access token_ for your account. To do this, you need to POST
the three tokens mentioned above to the login endpoint:
`api/isv/application/login`. The body of the POST request should be a JSON
string:

```json
{
  "data": {
    "type": "isvApplicationLogin",
    "attributes": {
      "clientId": <APPLICATION-KEY>,
      "clientSecret": <APPLICATION-SECRET>,
      "enterpriseId": <ENTERPRISE-ID>
    }
  }
}

```

If the credentials are correct, the HTTP response will have status code 201, and the body will be a JSON data structure:

```json
{
  "data": {
    "id": "1527b40212abb118a6d83a15",
    "type": "isvApplicationAuth",
    "attributes": {
      "accessToken": <ACCESS-TOKEN>
    }
  },
  "meta": {
    "createdTimestamp": 1588220310000
  }
}
```
The Access Token must be provided as an _Authorization_ header in calls to deploy code:

```
Authorization: Bearer <ACCESS-TOKEN>
```
See [send_code.py] for an example using the python requests module.

In order to send a Python application, it must be Base64 encoded. In [send_code.py], the application code is read from a file as a byte string and then base64 encoded, like this:
```python
import base64

with open("application.py", "rb") as f:
  code = f.read()

CODE_TO_DEPLOY = base64.b64encode(code).decode("utf-8")

```
This is the correct form for transmitting the code to the dock via the `docks\application\code` endpoint. The request body should look like this:
```json
{
  "data": {
    "type": "applicationCode",
    "attributes": {
      "dockId": <DOCK-ID>,
      "code": CODE_TO_DEPLOY
    }
  }
}

```



Send text message
-----------------
You can also send a text message to the dock. The message is displayed on the splashscreen. The message is sent to the `docks\application\message` endpoint. The request body should look like this:

```json
  {
     "data":{
        "type":"applicationMessage",
        "attributes":{
           "dockId":<DOCK-ID>,
           "message":"TEXT_MESSAGE_TO_DISPLAY"
        }
     }
   }
```

> **Warning**: Please make sure that the sent message starts with `t`. Otherwise, the message will not be consumed by the started application on the dock.


The `scripts/send_text.py` script can be used to send a text message to the dock:

```bash
   python3 ./scripts/send_text.py \
      -k <APPLICATION-KEY> \
      -s <APPLICATION-SECRET> \
      -e <ENTERPRISE-ID> \
      -d <DOCK-ID> \
      -t "Hello, World!"
```

Send image
----------
You can also send an image to the dock. The image is displayed on the splashscreen. The image is sent to the `docks\application\image` endpoint. The request body should look like this:

```json
  {
     "data":{
        "type":"applicationMessage",
        "attributes":{
           "dockId":<DOCK-ID>,
           "message":"RAW_IMAGE_DATA"
        }
     }
   }
```

> **Warning**: Please make sure that the raw image data starts with ``i``. Otherwise, the image will not be consumed by the started application on the dock.

The ``scripts/send_image.py`` script can be used to send an image to the dock:

```bash
   python3 ./scripts/send_image.py \
      -k <APPLICATION-KEY> \
      -s <APPLICATION-SECRET> \
      -e <ENTERPRISE-ID> \
      -d <DOCK-ID> \
      -f <LOCAL_PATH_TO_IMAGE_FILE>
```