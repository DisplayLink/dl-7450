# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) 2024 DisplayLink (UK) Ltd.

from datastore import KvStore
from mqtt import ErrorDescription, MqttClient
from splashscreen import Splashscreen, Alignment
from time import strftime
from wakeup import wakeup

class MqttApp:
    def __init__(self, broker, client_id):
        self.broker = broker
        self.client_id = client_id

        self.screen = Splashscreen()
        self.upper_text = ""
        self.lower_text = ""

        self.client = MqttClient(broker, client_id)
        self.client.on_subscribe(self.on_subscribe)
        self.client.on_message(self.on_message)
        self.subscribed_topics = {}

    # Text rendering

    def _render_text(self, upper_active: bool):
        upper = self.upper_text
        lower = self.lower_text
        if upper_active:
            lower = f'<span foreground="grey">{lower}</span>'
        else:
            upper = f'<span foreground="grey">{upper}</span>'

        text = f"<span size=\"small\"><b>{upper}\n\n{lower}</b></span>"
        layout = {
            "x": 960,
            "y": 650,
            "alignment": Alignment.MIDDLE
        }
        self.screen.add_text_box(text, layout)

    def text_upper(self, t):
        self.upper_text = t
        self._render_text(True)

    def text_lower(self, t):
        self.lower_text = t
        self._render_text(False)

    # Callbacks (appear as lower text)

    def on_connect(self, status: int, flags: dict):
        if (status == 0):
            self.text_lower(f"Connected to {self.broker} as {self.client_id}")
            self.subscribe_to_topic(f"{self.client_id}/interesting/topic/#", 2)
        else:
            error = ErrorDescription(status)
            raise Exception(f"Failed to connect to {self.broker} ({status}: {error})")

    def on_message(self, topic: str, message: bytes):
        self.text_lower(f"Received {topic}: {str(message, 'utf-8')}")
        # Send another message
        wakeup(self.send_hello_world_message, 4000)

    def on_subscribe(self, mid: int, qos: list):
        topic = self.subscribed_topics[mid]
        qos_as_str = ' ,'.join(str(q) for q in qos)
        self.text_lower(f"Subscribed to {topic} with ID {mid} and QoS {qos_as_str}")
        self.send_hello_world_message()

    # Actions (appear as upper text)

    def connect_to_broker(self, options: dict = {}):
        self.text_upper(f"Connecting to {self.broker} as {self.client_id}")
        self.client.connect(self.on_connect, options)

    def subscribe_to_topic(self, topic: str, qos: int):
        self.text_upper(f"Subscribing to {topic}")
        mid = self.client.subscribe((topic, qos))
        self.subscribed_topics[mid] = topic
        self.text_upper(f"Subscribe pending to {topic} with ID {mid}")

    def send_message(self, topic: str, message: str, qos: int):
        self.text_upper(f"Sending {topic}: {message}")
        self.client.publish(topic, message, qos)

    def send_hello_world_message(self):
        time_str = strftime("%H:%M:%S (%Z) %d/%m/%Y")
        message = f"Hello, World! at {time_str}"
        self.send_message(f"{self.client_id}/interesting/topic/news", message, 1)

    def run(self, trust_store=None):
        options = {"trust_store": trust_store}
        self.connect_to_broker(options)

BROKER = "mqtts://test.mosquitto.org:8886"
CLIENT_ID = KvStore().get("dock_name")
LETSENCRYPT_PEM = """\
-----BEGIN CERTIFICATE-----
MIIFBTCCAu2gAwIBAgIQS6hSk/eaL6JzBkuoBI110DANBgkqhkiG9w0BAQsFADBP
MQswCQYDVQQGEwJVUzEpMCcGA1UEChMgSW50ZXJuZXQgU2VjdXJpdHkgUmVzZWFy
Y2ggR3JvdXAxFTATBgNVBAMTDElTUkcgUm9vdCBYMTAeFw0yNDAzMTMwMDAwMDBa
Fw0yNzAzMTIyMzU5NTlaMDMxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBF
bmNyeXB0MQwwCgYDVQQDEwNSMTAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQDPV+XmxFQS7bRH/sknWHZGUCiMHT6I3wWd1bUYKb3dtVq/+vbOo76vACFL
YlpaPAEvxVgD9on/jhFD68G14BQHlo9vH9fnuoE5CXVlt8KvGFs3Jijno/QHK20a
/6tYvJWuQP/py1fEtVt/eA0YYbwX51TGu0mRzW4Y0YCF7qZlNrx06rxQTOr8IfM4
FpOUurDTazgGzRYSespSdcitdrLCnF2YRVxvYXvGLe48E1KGAdlX5jgc3421H5KR
mudKHMxFqHJV8LDmowfs/acbZp4/SItxhHFYyTr6717yW0QrPHTnj7JHwQdqzZq3
DZb3EoEmUVQK7GH29/Xi8orIlQ2NAgMBAAGjgfgwgfUwDgYDVR0PAQH/BAQDAgGG
MB0GA1UdJQQWMBQGCCsGAQUFBwMCBggrBgEFBQcDATASBgNVHRMBAf8ECDAGAQH/
AgEAMB0GA1UdDgQWBBS7vMNHpeS8qcbDpHIMEI2iNeHI6DAfBgNVHSMEGDAWgBR5
tFnme7bl5AFzgAiIyBpY9umbbjAyBggrBgEFBQcBAQQmMCQwIgYIKwYBBQUHMAKG
Fmh0dHA6Ly94MS5pLmxlbmNyLm9yZy8wEwYDVR0gBAwwCjAIBgZngQwBAgEwJwYD
VR0fBCAwHjAcoBqgGIYWaHR0cDovL3gxLmMubGVuY3Iub3JnLzANBgkqhkiG9w0B
AQsFAAOCAgEAkrHnQTfreZ2B5s3iJeE6IOmQRJWjgVzPw139vaBw1bGWKCIL0vIo
zwzn1OZDjCQiHcFCktEJr59L9MhwTyAWsVrdAfYf+B9haxQnsHKNY67u4s5Lzzfd
u6PUzeetUK29v+PsPmI2cJkxp+iN3epi4hKu9ZzUPSwMqtCceb7qPVxEbpYxY1p9
1n5PJKBLBX9eb9LU6l8zSxPWV7bK3lG4XaMJgnT9x3ies7msFtpKK5bDtotij/l0
GaKeA97pb5uwD9KgWvaFXMIEt8jVTjLEvwRdvCn294GPDF08U8lAkIv7tghluaQh
1QnlE4SEN4LOECj8dsIGJXpGUk3aU3KkJz9icKy+aUgA+2cP21uh6NcDIS3XyfaZ
QjmDQ993ChII8SXWupQZVBiIpcWO4RqZk3lr7Bz5MUCwzDIA359e57SSq5CCkY0N
4B6Vulk7LktfwrdGNVI5BsC9qqxSwSKgRJeZ9wygIaehbHFHFhcBaMDKpiZlBHyz
rsnnlFXCb5s8HKn5LsUgGvB24L7sGNZP2CX7dhHov+YhD+jozLW2p9W4959Bz2Ei
RmqDtmiXLnzqTpXbI+suyCsohKRg6Un0RC47+cpiVwHiXZAW+cn8eiNIjqbVgXLx
KPpdzvvtTnOPlC7SQZSYmdunr3Bf9b77AiC/ZidstK36dRILKz7OA54=
-----END CERTIFICATE-----
"""

app = MqttApp(BROKER, CLIENT_ID)
app.run(trust_store=LETSENCRYPT_PEM)
