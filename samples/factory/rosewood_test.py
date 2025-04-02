from datastore import CodeStore, ImageStore, KvStore
from dock import DockControl
from splashscreen import Splashscreen
from wakeup import wakeup


splashscreen = Splashscreen()


class Result:
    aborted = """<span color="red" weight="bold">Aborted</span>"""
    failure = """<span color="red" weight="bold">Failed</span>"""
    success = """<span color="green" weight="bold">Success</span>"""
    started = """<span color="orange" weight="bold">Started</span>"""


class Test:
    total_tests = 0

    def __init__(self, name):
        self.id = self.total_tests
        self.name = name
        Test.total_tests += 1
        self.start()

    def aborted(self):
        splashscreen.add_text_box(
            f"{self.name}: {Result.started}",
            {"x": 960, "y": 480 + (60 * self.id)},
        )

    def start(self):
        splashscreen.add_text_box(
            f"{self.name}: {Result.started}",
            {"x": 960, "y": 480 + (60 * self.id)},
        )

    def success(self):
        splashscreen.add_text_box(
            f"{self.name}: {Result.success}",
            {"x": 960, "y": 480 + (60 * self.id)},
        )

    def failure(self):
        splashscreen.add_text_box(
            f"{self.name}: {Result.failure}",
            {"x": 960, "y": 480 + (60 * self.id)},
        )


# Verbose testing of the ROM store, likely largely unnecessary - a subset should be sufficient to verify things have flashed correctly.
class TestFactorySettings:
    def __init__(self, on_fail, on_pass):
        self.key_store = KvStore()
        self.image_store = ImageStore()
        self.completed_checks = []
        self.on_pass = on_pass
        self.on_fail = on_fail
        self.test()

    def test(self):
        self.image_test = Test("Images")
        self.key_test = Test("Key Values")
        self.code_test = Test("Factory App")
        self.image_timer = wakeup(self.test_images, 0)
        self.key_timer = wakeup(self.test_key_values, 0)
        self.code_timer = wakeup(self.test_factory_app, 0)

    def show_next_image(self):
        if not self.images:
            self.image_timer.cancel()
            # self.on_pass(self.scenario)
            self.image_test.success()
            self.check_complete("images")
        else:
            image = self.images.pop()
            token = self.image_store.get_token(image)
            splashscreen.set_background(token)

    def test_images(self):
        self.images = self.image_store.list()
        expected_images = ["default"]
        if self.images != expected_images:
            self.image_timer = wakeup(self.show_next_image, 0, 2000)
        else:
            self.image_test.failure()
            self.abort()

    def test_key_values(self):
        self.keys = self.key_store.list()
        if self.keys != []:
            self.key_test.failure()
            self.abort()
        else:
            self.key_test.success()
            self.check_complete("key_values")

    def test_factory_app(self):
        self.code_store = CodeStore()
        checksum = self.code_store.info()["checksum"]
        if checksum != 2340183109:
            self.code_test.failure()
            self.abort()
        else:
            self.code_test.success()
            self.check_complete("factory_app")

    def abort(self):
        self.image_timer.cancel()
        self.key_timer.cancel()
        self.code_timer.cancel()
        self.on_fail("", "")

    def check_complete(self, check):
        self.completed_checks.append(check)
        if len(self.completed_checks) == 3:
            self.on_pass("")


class TestRosewood:
    def __init__(self):
        self.dock_control = DockControl()
        self.tests = [TestFactorySettings]

    def next_test(self):
        if self.tests:
            test_class = self.tests.pop()
            test = test_class(self.fail, self.passed)
        else:
            self.exit_test_mode(True)

    def fail(self, scenario, reason):
        splashscreen.add_text_box(
            f"Overall: {Result.failure}",
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
                f"Final result: {Result.success}",
                {"x": 960, "y": 800},
            )
            # self.dock_control.set_test_mode(False)

    def passed(self, scenario):
        self.next_test()


application = TestRosewood()
application.enter_test_mode()
