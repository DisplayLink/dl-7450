# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024-2025

from i2c import i2c, Bus
from splashscreen import Splashscreen
from wakeup import wakeup

class MCP9808:
    MCP_ID = 0x0054
    BASE_ADDRESS = 0x18
    TEMPERATURE_REGISTER_ADDRESS = 0x5
    MANUFACTURER_REGISTER = 0x06
    DEVICE_ID_REGISTER = 0x07
    REGISTER_SIZE = 2

    class TemperatureRegisterValue:
        number_of_fractional_bits = 4
        sign_bit_mask = 0x1000

        def __init__(self, value):
            self.value = int.from_bytes(value, "big")

        def _ambient_temperature_bits(self):
            return self.value & 0x0FFF

        def _unsigned_ambient_temperature(self):
            return self._ambient_temperature_bits() / (1 << self.number_of_fractional_bits)

        def _sign_bit(self):
            return bool(self.value & self.sign_bit_mask)

        def signed_ambient_temperature(self):
            temperature = self._unsigned_ambient_temperature()
            if self._sign_bit():
                temperature = 256 - temperature
            return temperature

    def __init__(self):
        self.i2c_bus = i2c(Bus.I2C1)
        self.device_id = self.read_device_id()

    def _read_byte(self, register):
        return self.i2c_bus.read(
            self.BASE_ADDRESS,
            register,
            self.REGISTER_SIZE
        )

    def read_device_id(self):
        data = self._read_byte(self.MANUFACTURER_REGISTER)
        man_id = data[0] << 8 | data[1]
        if man_id != self.MCP_ID:
            raise AssertionError(f"Unrecognised device on bus: {hex(id)}")

        data = self._read_byte(self.DEVICE_ID_REGISTER)
        device_id = data[0]
        device_rev = data[1]
        if device_id != 0x04:
            raise AssertionError(f"Unrecognised device id: {hex(device_id)}")
        return f"MCP9808 rev {device_rev}"

    def read_temperature(self):
        data = self._read_byte( self.TEMPERATURE_REGISTER_ADDRESS)
        temperature_register_value = self.TemperatureRegisterValue(data)
        return temperature_register_value.signed_ambient_temperature()


class Application:
    def __init__(self):
        self.sensor = MCP9808()
        self.screen = Splashscreen()
        self.timer = None

    def read_next_temperature(self):
        temperature = self.sensor.read_temperature()

        msg = [
            self.sensor.device_id,
            f"Temperature: {temperature:.2f}℃"
        ]

        self.screen.add_text_box(msg)
        self.timer = wakeup(self.read_next_temperature, 2000)

    def run(self):
        self.read_next_temperature()


app = Application()
app.run()
