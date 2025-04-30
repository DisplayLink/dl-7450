# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) 2024-2025 DisplayLink (UK) Ltd.

from datastore import KvStore
from mqtt import ErrorDescription, MqttClient
from splashscreen import Splashscreen, Alignment
from time import strftime
from wakeup import wakeup


class MessageStatus:
    UNKNOWN = 0
    WAITING_FOR_RESPONSE = 1
    MESSAGE_QUEUED = 2


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
        self.message_status = MessageStatus.UNKNOWN

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
            self.message_status = MessageStatus.UNKNOWN
            self.text_lower(f"Connected to {self.broker} as {self.client_id}")
            self.subscribe_to_topic(f"{self.client_id}/interesting/topic/#", 2)
        else:
            error = ErrorDescription(status)
            self.text_lower(f"Failed to connect to broker ({status}: {error} - reconnecting)")

    def on_message(self, topic: str, message: bytes):
        self.text_lower(f"Received {topic}: {str(message, 'utf-8')}")
        # Send another message
        if self.message_status == MessageStatus.WAITING_FOR_RESPONSE:
            self.message_status = MessageStatus.MESSAGE_QUEUED
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
        self.message_status = MessageStatus.WAITING_FOR_RESPONSE
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
MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw
TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
cmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwHhcNMTUwNjA0MTEwNDM4
WhcNMzUwNjA0MTEwNDM4WjBPMQswCQYDVQQGEwJVUzEpMCcGA1UEChMgSW50ZXJu
ZXQgU2VjdXJpdHkgUmVzZWFyY2ggR3JvdXAxFTATBgNVBAMTDElTUkcgUm9vdCBY
MTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAK3oJHP0FDfzm54rVygc
h77ct984kIxuPOZXoHj3dcKi/vVqbvYATyjb3miGbESTtrFj/RQSa78f0uoxmyF+
0TM8ukj13Xnfs7j/EvEhmkvBioZxaUpmZmyPfjxwv60pIgbz5MDmgK7iS4+3mX6U
A5/TR5d8mUgjU+g4rk8Kb4Mu0UlXjIB0ttov0DiNewNwIRt18jA8+o+u3dpjq+sW
T8KOEUt+zwvo/7V3LvSye0rgTBIlDHCNAymg4VMk7BPZ7hm/ELNKjD+Jo2FR3qyH
B5T0Y3HsLuJvW5iB4YlcNHlsdu87kGJ55tukmi8mxdAQ4Q7e2RCOFvu396j3x+UC
B5iPNgiV5+I3lg02dZ77DnKxHZu8A/lJBdiB3QW0KtZB6awBdpUKD9jf1b0SHzUv
KBds0pjBqAlkd25HN7rOrFleaJ1/ctaJxQZBKT5ZPt0m9STJEadao0xAH0ahmbWn
OlFuhjuefXKnEgV4We0+UXgVCwOPjdAvBbI+e0ocS3MFEvzG6uBQE3xDk3SzynTn
jh8BCNAw1FtxNrQHusEwMFxIt4I7mKZ9YIqioymCzLq9gwQbooMDQaHWBfEbwrbw
qHyGO0aoSCqI3Haadr8faqU9GY/rOPNk3sgrDQoo//fb4hVC1CLQJ13hef4Y53CI
rU7m2Ys6xt0nUW7/vGT1M0NPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNV
HRMBAf8EBTADAQH/MB0GA1UdDgQWBBR5tFnme7bl5AFzgAiIyBpY9umbbjANBgkq
hkiG9w0BAQsFAAOCAgEAVR9YqbyyqFDQDLHYGmkgJykIrGF1XIpu+ILlaS/V9lZL
ubhzEFnTIZd+50xx+7LSYK05qAvqFyFWhfFQDlnrzuBZ6brJFe+GnY+EgPbk6ZGQ
3BebYhtF8GaV0nxvwuo77x/Py9auJ/GpsMiu/X1+mvoiBOv/2X/qkSsisRcOj/KK
NFtY2PwByVS5uCbMiogziUwthDyC3+6WVwW6LLv3xLfHTjuCvjHIInNzktHCgKQ5
ORAzI4JMPJ+GslWYHb4phowim57iaztXOoJwTdwJx4nLCgdNbOhdjsnvzqvHu7Ur
TkXWStAmzOVyyghqpZXjFaH3pO3JLF+l+/+sKAIuvtd7u+Nxe5AW0wdeRlN8NwdC
jNPElpzVmbUq4JUagEiuTDkHzsxHpFKVK7q4+63SM1N95R1NbdWhscdCb+ZAJzVc
oyi3B43njTOQ5yOf+1CceWxG1bQVs5ZufpsMljq4Ui0/1lvh+wjChP4kqKOJ2qxq
4RgqsahDYVvTH9w7jXbyLeiNdd8XM2w9U/t7y0Ff/9yi0GE44Za4rF2LN9d11TPA
mRGunUHBcnWEvgJBQl9nJEiU0Zsnvgc/ubhPgXRR4Xq37Z0j4r7g1SgEEzwxA57d
emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=
-----END CERTIFICATE-----
"""

app = MqttApp(BROKER, CLIENT_ID)
app.run(trust_store=LETSENCRYPT_PEM)
