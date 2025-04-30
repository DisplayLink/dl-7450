# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2025

from iperf import IperfClient
from splashscreen import Splashscreen


splashscreen = Splashscreen()


class IperfClientRunner:
    def __init__(self, hostname: str, port: int):
        self.iperf = IperfClient(hostname, port)
        self.running = False

    def _display_result(self, result: dict):
        self.running = False
        bitrates = [interval["sum"]["bits_per_second"] for interval in result["intervals"]]
        bitrates_kb = [b / 1000 for b in bitrates]
        average_bitrate_kb = sum(bitrates_kb) / len(bitrates_kb) if bitrates_kb else 0
        text = ["Results:"]
        text.extend(f"{i}: {b:.2f}" for i, b in enumerate(bitrates_kb))
        text.append(f"Average: {average_bitrate_kb:.2f} Kbps")
        if "error" in result:
            text.append(f"Error: {result['error'][:60]}...")
        splashscreen.add_text_box(text)

    def run(self):
        if self.running:
            raise Exception("Test already running")
        self.running = True
        splashscreen.add_text_box("Running iperf test...")
        self.iperf.run(on_complete=self._display_result)


SERVER_NAME = "iperf-server"
SERVER_PORT = 5000


test = IperfClientRunner(SERVER_NAME, SERVER_PORT)
test.run()
