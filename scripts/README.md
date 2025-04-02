# Using the DisplayLink REST API to support development

When you receive your evaluation DL-7450 board, you will also receive some
pieces of information that are required to make use of the DisplayLink REST
endpoints for development services.  Your account is identified by the
following tokens

 * `ENTERPRISE-ID`. This is a token to identify the entity that owns the
   DL-7450. It is unique to your organisation, and serves to ensure that code
   can only be deployed to docks that you own.
 * `APPLICATION-KEY` and `APPLICATION-SECRET`. You can think of these as a
   username and password. They are secrets that are used as authentication
   tokens. They will be provided to you securely via the usual mechanisms for
   distributing DisplayLink artefacts to customers. Please treat these tokens
   as secret and do not distribute to anyone who is not authorised to deploy
   code to the DL-7450 evaluation board.

In addition, you will be provided with an identifier that is unique to the
reference board that you have been provided with:
```
DOCK-ID = "BC385DB79E2B94DC70E44422FCFFB29C0D90FCA7F024AC72625D7376233CFC02"
```
These four pieces of information enable access to the development services located at
`https://sandbox.vision.synaptics.com/api`.

## Deploying code for immediate testing

The `docks\application\code` endpoint is a mechanism to send a Python
application to the dock for immediate deployment. The [send_code.py] script is
a helper script for POSTing code to this endpoint and can be invoked as follows:


```bash
python3 ./send_code.py -k <APPLICATION-KEY> -s <APPLICATION-SECRET> -e <ENTERPRISE-ID> -d <DOCK-ID> -f myapplication.py
```

You are free to use this script, or to design your own mechanism to deploy the
code, based on this script. For completeness we provide a description of the
deployment process.  Code is sent to a DL-7450 by making an HTTP POST request
to a REST endpoint in the DisplayLink development server,  There are two steps.

First, obtain an _access token_ for your account. To do this, you need to POST
the three tokens mentioned above to the login endpoint:
`/isv/application/login`. The body of the POST request should be a JSON
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

If the credentials are correct, the HTTP response will have status code 201,
and the body will be a JSON data structure:

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
See [send_code.py] for an example using the python *requests* module.

In order to send a Python application, it must be Base64 encoded. In
[send_code.py], the application code is read from a file as a byte string and
then base64 encoded, like this:

```python
import base64

with open("application.py", "rb") as f:
  code = f.read()

CODE_TO_DEPLOY = base64.b64encode(code).decode("utf-8")

```
This is the correct form for transmitting the code to the dock via the
`docks\application\code` endpoint. The request body should look like this:
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

# Rewrite Application ROM Store

The `docks\application\romstore` endpoint is a mechanism to rewrite the
Application ROM store on the dock. This is an atomic and destructive operation;
i.e. it will completely replace the existing contents of the ROM store. You can
recover the ROM store to the state it was in when you received the reference
board - see below.

A helper script, [send_rom_store.py], is provided. 

```bash
python3 send_rom_store.py -k <APPLICATION-KEY> -s <APPLICATION-SECRET> -e <ENTERPRISE-ID> -d <DOCK-ID> -c <ROM_STORE_CONFIG_FILE> 
```
The application key and secret and the enterprise ID are the same as described
above in the section on sending code, and are used in the same way to obtain an
application access token. The POST request to the endpoint is as follows:

```json
{
  "data": {
    "type": "applicationRomStore",
    "attributes": {
      "dockId": DOCK_ID.value,
      "code": {
        "code": <BASE64_ENCODED_APPLICATION_CODE>
      },
      "kvStore": {
        "dock_name": "mydock",
        "timezone": "CST"
      },
      "images": {
        "mypng": {
          "type": "PNG",
          "data": <BASE64_ENCODED_IMAGE_DATA>
        },
        "mybmp": {
          "type": "BMP",
          "data": <BASE64_ENCODED_IMAGE_DATA>
        },
        "myjpeg": {
          "type": "JPEG",
          "data": <BASE64_ENCODED_IMAGE_DATA>
        }
      }
    }
  }
}
```

The [send rom store script](send_rom_store.py) does a lot of the heavy-lifting
involved in constructing this request.  Application developers can maintain a
local version of the datastore and explain it in the YAML
*ROM_STORE_CONFIG_FILE* that is passed to the script. A prototype of such a
YAML file is given in the [sample ROM store
config](rom_store_sample/rom_store_config_sample.yaml), and a full working
example which restores the original settings is given in the [restore default
ROM store script](rom_store_default/config.yaml).

Files can either be specified as absolute paths or, by starting a path with
`${CONFIG_PATH}`, as relative paths relative to the config.

Please note, the request is schema checked carefully, and if any of the data is
not in the correct format, the HTTP response code will be 400. Check the
following:
 * The Key-Value entries must be strings, both the key and the value;
 * The image data must be correct for the stated type. For example, if the
   request states that the image is a JPEG image, then the data (prior to
   base64 encoding) must be a valid JPEG image in binary format. 
 
To restore the Application ROM store to the settings that it was in when you
received the reference board, please use the [rom_store_default/config.yaml]
script. The *dock_name* provided should be indicated on the board on a label,
such as *RW02-0005*, but you can choose another name and another timezone if
you so wish.


Send application data
---------------------
The [Internet-of-things sample scripts](../samples/iot) give examples where
the DisplayLink development REST API is used to send application-specific data
to the dock, via the `docks\application\message` endpoint.

```json
  {
     "data":{
        "type":"applicationMessage",
        "attributes":{
           "dockId":<DOCK-ID>,
           "message": <APPLICATION_DATA>
        }
     }
   }
```

This endpoint is provided for convenience in evalutating the DL-7450 SDK, so
that application developers do not need to immediately set up the machinery for
communicating with IoT brokers. These particular applications can receive a
text message through this mechanism, and it simply displays it on the screen.
The message should be prepended with the character `t` and then base64 encoded.
The [send text script](send_text.py) can be used to send a text message to a
dock running this application:

```bash
   python3 ./scripts/send_text.py \
      -k <APPLICATION-KEY> \
      -s <APPLICATION-SECRET> \
      -e <ENTERPRISE-ID> \
      -d <DOCK-ID> \
      -t "Hello, World!"
```

The [text and image sample](../samples/iot/text_and_image.py) can also receive
an image, which is used to replace the splashscreen background. In this case
the image must be a PNG, which is first prepended with the character `i` and
then base 64 encoded. The [send image script](send_image.py) script can be used
to send an image to the dock running this application.

```bash
   python3 ./scripts/send_image.py \
      -k <APPLICATION-KEY> \
      -s <APPLICATION-SECRET> \
      -e <ENTERPRISE-ID> \
      -d <DOCK-ID> \
      -f <LOCAL_PATH_TO_IMAGE_FILE>
```

Application developers are free to experiment with send data to a dock using
the application message endpoint, and should be careful to coordinate the input
data with the application running on the dock.
