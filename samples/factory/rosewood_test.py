from datastore import CodeStore, ImageStore, KvStore
from dock import DockControl
from iperf import IperfClient
from splashscreen import Splashscreen
from wakeup import wakeup


splashscreen = Splashscreen()


# Test infrastructure


class Result:
    @staticmethod
    def _make_span(color, text, extra=None):
        if extra:
            text = f"{text} ({extra})"
        return f'<span color="{color}" weight="bold">{text}</span>'

    @classmethod
    def aborted(cls, extra=None):
        return cls._make_span("red", "Aborted", extra=extra)

    @classmethod
    def failure(cls, extra=None):
        return cls._make_span("red", "Failed", extra=extra)

    @classmethod
    def success(cls, extra=None):
        return cls._make_span("green", "Success", extra=extra)

    @classmethod
    def started(cls, extra=None):
        return cls._make_span("orange", "Started", extra=extra)


class TestDisplay:
    total_tests = 0

    def __init__(self, name):
        self.id = self.total_tests
        self.name = name
        type(self).total_tests += 1
        self.start()

    def aborted(self, extra=None):
        splashscreen.add_text_box(
            f"{self.name}: {Result.aborted(extra=extra)}",
            {"x": 960, "y": 480 + (60 * self.id)},
        )

    def start(self, extra=None):
        splashscreen.add_text_box(
            f"{self.name}: {Result.started(extra=extra)}",
            {"x": 960, "y": 480 + (60 * self.id)},
        )

    def success(self, extra=None):
        splashscreen.add_text_box(
            f"{self.name}: {Result.success(extra=extra)}",
            {"x": 960, "y": 480 + (60 * self.id)},
        )

    def failure(self, extra=None):
        splashscreen.add_text_box(
            f"{self.name}: {Result.failure(extra=extra)}",
            {"x": 960, "y": 480 + (60 * self.id)},
        )


class TestCase:
    def __init__(self, test_name: str, suite):
        self.name = test_name
        self.suite = suite
        self.display = TestDisplay(test_name)
        self.display.start()
        self.timer = wakeup(self.run, 0)

    def run(self):
        raise NotImplementedError()

    def success(self, extra=None):
        self.display.success(extra=extra)
        self.suite.check_complete(self.name)

    def fail(self, extra=None):
        self.display.failure(extra=extra)
        self.suite.abort()


class TestSuite:
    def __init__(self, on_fail, on_pass):
        self.test_cases = []
        self.completed_checks = []
        self.on_pass = on_pass
        self.on_fail = on_fail
        self.test()

    def register_test(self, test_class: type, test_name: str):
        test_case = test_class(test_name, self)
        self.test_cases.append(test_case)

    def test(self):
        raise NotImplementedError()

    def abort(self):
        for case in self.test_cases:
            case.timer.cancel()
        self.on_fail("", "")

    def check_complete(self, check):
        self.completed_checks.append(check)
        if len(self.completed_checks) == len(self.test_cases):
            self.on_pass("")


# Tests


class TestImages(TestCase):
    EXPECTED_IMAGES = ["default"]

    def show_next_image(self):
        if not self.images:
            self.timer.cancel()
            # self.on_pass(self.scenario)
            self.success()
        else:
            image = self.images.pop()
            token = self.image_store.get_token(image)
            splashscreen.set_background(token)

    def run(self):
        image_store = ImageStore()
        self.images = image_store.list()
        if self.images != self.EXPECTED_IMAGES:
            self.timer = wakeup(self.show_next_image, 0, 2000)
        else:
            self.fail()


class TestKeyValues(TestCase):
    EXPECTED_KEY_STORE = []

    def run(self):
        key_store = KvStore()
        keys = key_store.list()
        if keys != self.EXPECTED_KEY_STORE:
            self.fail()
        else:
            self.success()


class TestFactoryApp(TestCase):
    EXPECTED_FACTORY_CHECKSUM = 2340183109

    def run(self):
        code_store = CodeStore()
        checksum = code_store.info()["checksum"]
        if checksum != self.EXPECTED_FACTORY_CHECKSUM:
            self.fail()
        else:
            self.success()


# Verbose testing of the ROM store, likely largely unnecessary - a subset should be sufficient to verify things have flashed correctly.
class TestFactorySettings(TestSuite):
    def test(self):
        self.register_test(TestImages, "Images")
        self.register_test(TestKeyValues, "Key Values")
        self.register_test(TestFactoryApp, "Factory App")


class TestIperf(TestCase):
    BITRATE_THRESHOLD_MB = 50

    def _iperf_complete(self, result):
        if not result.get("intervals", False):
            self.fail()
        else:
            bitrates = [interval["sum"]["bits_per_second"] for interval in result["intervals"]]
            bitrates_mb = [b / 1000**2 for b in bitrates]
            average_bitrate_mb = sum(bitrates_mb) / len(bitrates_mb)
            average_bitrate_text = f"Average: {average_bitrate_mb:.2f} Mbps"
            if average_bitrate_mb < self.BITRATE_THRESHOLD_MB:
                self.fail(extra=average_bitrate_text)
            else:
                self.success(extra=average_bitrate_text)

    def run(self):
        self.iperf_client = IperfClient(self.suite.SERVER_HOSTNAME, self.suite.SERVER_PORT)
        self.iperf_client.run(on_complete=self._iperf_complete)


class TestBandwidth(TestSuite):
    SERVER_HOSTNAME = "iperf-server"
    SERVER_PORT = 5000

    def test(self):
        self.register_test(TestIperf, "Iperf")


class TestRosewood:
    def __init__(self):
        self.dock_control = DockControl()
        self.tests = [
            TestFactorySettings,
            TestBandwidth,
        ]

    def next_test(self):
        if self.tests:
            test_class = self.tests.pop(0)
            test = test_class(self.fail, self.passed)
        else:
            self.exit_test_mode(True)

    def fail(self, scenario, reason):
        splashscreen.add_text_box(
            f"Overall: {Result.failure()}",
            {"x": 960, "y": 800},
        )
        self.exit_test_mode(False)

    def enter_test_mode(self):
        splashscreen.add_text_box("ROSEWOOD TEST MODE")
        # self.dock_control.set_test_mode(True)
        wakeup(self.next_test, 2000)

    def exit_test_mode(self, passed):
        if passed:
            splashscreen.add_text_box(
                f"Final result: {Result.success()}",
                {"x": 960, "y": 800},
            )
            # self.dock_control.set_test_mode(False)

    def passed(self, scenario):
        self.next_test()


application = TestRosewood()
application.enter_test_mode()
