# Creating Internet-of-Things Docks

The DL-7450 SDK allows application developers to purpose docking stations as
Internet-of-Things (IoT) devices. The [main application](text_message.py) in this
tutorial is very simple, but in order to make it work a certain amount of
preparation needs to be carried out. Before explaining that, let's consider
some of the general principles required to create an IoT device.


## Provisioning and security of Iot Devices

In order to create a secure and reliable Internet-of-Things ecosystem, several
considerations must be made in the manufacturing, provisioning and
commissioning of devices. Synaptics has designed the DL-7450 chip with
guidelines provided by [FIDO Alliance](https://fidoalliance.org/) and the
[Internet-of-Things Security Foundation](https://iotsecurityfoundation.org/)
(IoTSF) in mind.

First, an IoT device requires a unique, immutable and unforgeable identity,
managed in a secure trust zone somewhere on the device - a *Physical
Uncloneable Function* or PUF. The DL-7450 delivers this out-of-the box. The
*One-Time Programmable* memory area on the chip provides these unique
identities out-of-the box. The OTP is only able to be read by a *secure
processor* in the chip, and is therefore fenced inside a secure trust zone on
the chip.

Second, other entities in the IoT ecosystem, such as a central broker, must be
able to authenticate an IoT device prior to communicating with it.
Manufacturers can provision a DL-7450 with a TLS certificate bound to the
dock's unique identity and signed by an authority that they trust. All of the
cryptography is carried out in the secure zone by the security processor.

Finally, once the DL-7450 has been purchased, the SDK can be used to carry out
a final registration or proof of ownership step, and then for ongoing
communication within its own network.

To give this generic discussion some definiteness, these steps could be used to
purpose a DL-7450 to be a client device in an Azure IoT hub instance:

 * In the manufacturer's factory process, a unique client certificate can be
   created and signed by an authority trusted by the manufacturer and
   recognised by their Azure IoT hub Device Provisioning Service (DPS). This
   information can be stored in the factory persistent storage area.
 * The manufacturer can also store a start up Python application that connects
   to the DPS using the Azure DPS Client library from the DL-7450 SDK.
 * When the dock first boots after purchase, the startup app will connect to
   DPS, and complete the registration process. The artefacts created in the
   registration step can then be stored in the runtime persistent storage area.
 * Subsequently, the dock can use the Azure IoT Client library from the DL-7450
   SDK to send and retrieve data via the DeviceTwin or messaging mechanisms and
   participate in the manufacturer's IoT network.

## DL-7450 SDK Workshop

To demonstrate the IoT capability of the DL-7450, we use our development cloud
service. A customer can create an account with the service and register docks
to that account. For each dock in the workshop we have created such an account
and registered the single dock to that account. The development backend has a
REST interface, and we have developed the simple web page as a front end. To
access the API, the front end obtains an access token from the backend and can
then route messages through to the dock. That's how we send the Python
application code to the docks. There is a simple application message endpoint
where the control application can send free form messages. The message routes
through the backend and is then sent via MQTT to the dock. The `vision_client`
module in the DL-7450 SDK enables the Python application to register a message
handler.

The front end code looks something like this:

```python

def send_application_message(request, dockId, application_message: bytes):
  extra_headers = {"Authorization": f"Bearer {access_token(request)}"}

  payload = {
    "data": {
      "type": "applicationMessage",
      "attributes": {
        "dockId": dockId,
        "message": base64.b64encode(application_message).decode("utf-8"),
      },
    }
  }

  response = requests.post(
    API + f"/docks/application/message", json=payload, headers=extra_headers
  )

  print(f"Message Sent: {response.status_code}")
  return response

@app.route("/text", methods=["POST"])
@jwt_required()
def post_text_message():
  data = request.json
  text = data["message"]
  dock_id = data["dockId"]

  message = bytes("t" + text, encoding="utf-8")
  response = send_application_message(request, dock_id, message)
  return {}, response.status_code
```

In other words, the text string is prepended with the ASCII character `t` and
the resulting string sent as a byte array. Other data can be sent prepended
with `i` for image and `f` for firmware blob. These cases are not shown in the
workshop.

We use the DL-7450 `vision_client` module to register a handler for application messages


```python

def run(self):
  # ...
  self.client = VisionClient()
  self.client.on_message(self.handle_message)

def handle_message(self, message):
  messageType = message[0]
  message = message[1:]

  # Check messageType is "t"
  if messageType == 116:
    self.show_text(str(message, "utf-8"))
  else:
    self.show_text("<b>Unknown message type</b>")
```
When passing slices of objects such as `bytearray` instances, Python creates a
copy which involves allocation of the size proportional to the size of slice.
This can be alleviated using a `memoryview` object.

```python

def cb(message):
    messageType = message[0]   # a copy is passed
    message = message[1:]

    mv = memoryview(message)   # small object is allocated
    messageType = mv[0]
    message = mv[1:]           # a pointer to memory is passed

```

As stated at the beginning of this README, the code is very simple, but
requires prior registering of the device to the cloud provider, in this case
our development backend.
