from dock import DockControl, DockInfo
from splashscreen import Splashscreen
from wakeup import wakeup

dock_control = DockControl()
dock_info = DockInfo()
splashscreen = Splashscreen()


class HostConnection:
    host_status = dock_info.host_status()
    timer = None

    def __init__(self):
        self.display_connection_status()

    @staticmethod
    def grant_access():
        splashscreen.add_text_box("Granting access")
        dock_control.suspend_host_connection(False)

    @staticmethod
    def revoke_access():
        splashscreen.add_text_box("Revoking access")
        dock_control.suspend_host_connection(True)

    def display_connection_status(self):
        if self.host_status == dock_info.HOST_CONNECTED:
            splashscreen.add_text_box("Host Connected")
        elif self.host_status == dock_info.HOST_CONNECTION_SUSPENDED:
            splashscreen.add_text_box("Access revoked")
        elif self.host_status == dock_info.HOST_NOT_CONNECTED:
            splashscreen.add_text_box("No host connected")

    def revoke_access_on_connection(self):
        previous_status = self.host_status
        self.host_status = dock_info.host_status()
        if previous_status != self.host_status:

            if self.host_status == dock_info.HOST_CONNECTED:
                # If we have just connected a dock, suspend the connection.
                if previous_status == dock_info.HOST_NOT_CONNECTED:
                    self.revoke_access()
                else:
                    self.display_connection_status()
            elif self.host_status == dock_info.HOST_CONNECTION_SUSPENDED:
                # After successfully suspending, resume connection after 10 seconds.
                splashscreen.add_text_box("Access revoked for 10 seconds")
                self.timer = wakeup(self.grant_access, 10000)
            elif self.host_status == dock_info.HOST_NOT_CONNECTED:
                if self.timer is not None:
                    self.timer.cancel()
                self.display_connection_status()


host_connection = HostConnection()
gc_prevention = wakeup(host_connection.revoke_access_on_connection, 500, 500)
