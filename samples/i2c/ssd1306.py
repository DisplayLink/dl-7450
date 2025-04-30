# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2024-2025

from i2c import i2c

# Datasheet: https://www.hpinfotech.ro/SSD1309.pdf


class MonochromeImage:
    def __init__(self, data) -> None:
        self.height = len(data)
        self.width = len(data[0]) if self.height else 0
        self.image_data = b''.join(data)

    def __getitem__(self, key) -> int:
        y, x = key
        if (x < 0) or (x >= self.width) or (y < 0) or (y >= self.height):
            return 0
        return self.image_data[y * self.width + x]


synaptics_logo = MonochromeImage((
    b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\1\1\1\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0\1\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0\1\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\0\0\1\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\1\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\1\0\0\0\0\0\0\1\1\0\1\0\0\0\0\0\0\0\0\0\0\0\1\1\0\0\0\0',
    b'\0\0\0\1\0\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0',
    b'\0\0\0\0\1\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\1\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\0\0',
    b'\0\0\0\0\1\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\1\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\1\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\1\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\1\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\1\1\1\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0\0\0\0\0\0\0\1\1\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\1\1\1\0\0\0\0\0\0\0\0\0\0\1\1\0\1\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\1\0\1\1\0\0\0\0\0\0\1\1\0\1\1\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\1\1\0\1\1\1\1\1\1\0\1\1\0\0\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\0\1\1\0\1\0\1\0\1\1\0\0\0\0\0\0\0\0\0\0\0',
    b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\1\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0',
))


def ceiling_divide(dividend, divisor):
    return -(dividend // -divisor)


class SSD1306:
    I2C_ADDRESS = 0x3C
    COMMAND_ADDRESS = 0x00
    DATA_ADDRESS = 0x40
    NUM_OF_COL = 128
    NUM_OF_PAGES = 8
    PAGE_SIZE = 8

    # Fundamental commands from Table 9.1 of datasheet
    CONTRAST_CONTROL = b'\x81'
    ENTIRE_DISPLAY_ON = b'\xA4'
    NORMAL_DISPLAY = b'\xA6' # i.e. inversion off
    INVERSE_DISPLAY = b'\xA7'
    DISPLAY_OFF = b'\xAE'
    DISPLAY_ON = b'\xAF'
    CHARGE_PUMP = b'\x8D'

    # Scrolling commands from Table 9.2 of datasheet
    SCROLL_RIGHT = b'\x26'
    SCROLL_LEFT = b'\x27'
    RIGHT_VERTICAL_SCROLL = b'\x29'
    LEFT_VERTICAL_SCROLL = b'\x2A'
    DISABLE_SCROLLING = b'\x2E'
    ENABLE_SCROLLING = b'\x2F'

    # Addressing commands from Table 9.3 of datasheet
    MEMORY_ADDRESSING_MODE = b'\x20'
    COLUMN_ADDRESS = b'\x21'
    PAGE_ADDRESS = b'\x22'
    DISPLAY_START_LINE = b'\x40'
    SEGMENT_MAP_FLIP = b'\xA1'
    MULTIPLEX_RATIO = b'\xA8'
    COM_OUTPUT_SCAN_NORMAL = b'\xC0'
    COM_OUTPUT_SCAN_FLIP = b'\xC8'
    DISPLAY_OFFSET = b'\xD3'
    COM_PINS_HW_CONFIG = b'\xDA'

    # Timing and driving scheme commands from Table 9.5 of datasheet
    DISPLAY_CLOCK_DIV = b'\xD5'
    PRECHARGE_PERIOD = b'\xD9'
    VCOM_DESELECT_LEVEL = b'\xDB'

    def __init__(self) -> None:
        self.i2c_device = i2c()

        init_commands = (
            self.DISPLAY_OFF,
            self.DISPLAY_CLOCK_DIV + b'\x80',
            self.MULTIPLEX_RATIO + b'\x3F',
            self.DISPLAY_OFFSET + b'\x00',
            self.DISPLAY_START_LINE,
            self.CHARGE_PUMP + b'\x14',
            self.MEMORY_ADDRESSING_MODE + b'\x00', # Memory mode: horizontal addressing
            self.SEGMENT_MAP_FLIP,
            self.COM_OUTPUT_SCAN_FLIP,
            self.COM_PINS_HW_CONFIG + b'\x12',
            self.CONTRAST_CONTROL + b'\xCF',
            self.PRECHARGE_PERIOD + b'\xF1',
            self.VCOM_DESELECT_LEVEL + b'\x40',
            self.ENTIRE_DISPLAY_ON,
            self.NORMAL_DISPLAY,
            self.DISPLAY_ON
        )

        for command in init_commands:
           self.send_command(command)

    def send_command(self, command: bytes)-> None:
        self.i2c_device.write(self.I2C_ADDRESS, self.COMMAND_ADDRESS, command)

    def send_data(self, data: bytes)-> None:
        self.i2c_device.write(self.I2C_ADDRESS, self.DATA_ADDRESS, data)

    def clear_screen(self) -> None:
        self.disable_scrolling()
        # Draw across entire screen
        self.set_draw_area(0, 0, self.NUM_OF_COL, self.NUM_OF_PAGES)
        for page in range(self.NUM_OF_PAGES):  # Clear all pages
            # Column address from 0 to 127
            self.send_command(self.COLUMN_ADDRESS + b'\x00\x7F')
            self.send_command(self.PAGE_ADDRESS + bytes([page, page]))
            # Clear the page by zeroing all columns
            self.send_data(b'\x00' * self.NUM_OF_COL)

    def write_char(self, x, y_pages, char_data):
        # Write the 8 bytes of the character (this is a very basic example for 8x8 font)
        self.set_draw_area(x, y_pages, 8, 1)
        self.send_data(bytes(char_data))

    def write_text(self, x, y_pages, text):
        current_x = x
        current_y = y_pages
        for char in text:
            ascii_val = ord(char)
            if ascii_val in ascii_font:
                char_data = ascii_font[ascii_val]
                self.write_char(current_x, current_y, char_data)
                # Move the x position for the next character (each character is 8 pixels wide)
                current_x += 8
                # If the x position goes beyond the screen width (128 pixels), wrap to the next line
                if current_x > 127:
                    current_x = 0
                    current_y += 1  # Move to the next page (next row of text)
                    if current_y > 7:  # If we exceed the display height, stop
                        break


    def set_draw_area(self, x, y_pages, width, height_pages):
        # Set column address (x position)
        x_start = x
        x_end = x_start + width - 1
        self.send_command(self.COLUMN_ADDRESS + bytes([x_start, x_end]))
        # Set page address (y position)
        y_start = y_pages
        y_end = y_start + height_pages - 1
        self.send_command(self.PAGE_ADDRESS + bytes([y_start, y_end]))

    def show_image(self, image: MonochromeImage, x=0, y_pages=0):
        self.disable_scrolling()
        # Draw just on specified area
        height_pages = ceiling_divide(image.height, self.PAGE_SIZE)
        self.set_draw_area(x, y_pages, image.width, height_pages)
        for row_start in range(0, image.height, self.PAGE_SIZE):
            page_buffer = b''
            # Send the contents of each page column by column
            for col in range(image.width):
                # Send the contents of each column row by row
                col_pixels = sum(image[row_start + row_in_page, col] << row_in_page for row_in_page in range(self.PAGE_SIZE))
                page_buffer += col_pixels.to_bytes(1, 'big')
            self.send_data(page_buffer)
            y_pages += 1

    def horizontal_scroll(self, right = True):
        direction = self.SCROLL_RIGHT if right else self.SCROLL_LEFT
        self.send_command(
            direction + 
            b'\x00'  # Dummy byte
            b'\x00'  # Start page
            b'\x00'  # Time interval
            b'\x07'  # End page
            b'\x00'  # Dummy byte
            b'\x00'  # Start column
            b'\x7F'  # End column
        )

        #  Start scrolling
        self.send_command(self.ENABLE_SCROLLING)

    def vertical_scroll(self, up = True):
        direction = b'\x01' if up else b'\x3F'
        self.send_command(
            self.RIGHT_VERTICAL_SCROLL +
            b'\x00'  # Dummy byte
            b'\x00'  # Start page
            b'\x00'  # Time interval
            b'\x07'  # End page
            + direction + 
            b'\x00'  # Start column
            b'\x7F'  # End column
        )

        #  Start scrolling
        self.send_command(self.ENABLE_SCROLLING)

    def disable_scrolling(self):
        self.send_command(self.DISABLE_SCROLLING)


class Application:
    def __init__(self):
        self.oled = SSD1306()

    def show_logo(self):
        self.oled.clear_screen()
        self.oled.show_image(synaptics_logo, x=48, y_pages=2)
        self.oled.horizontal_scroll(right = True)
        #self.oled.vertical_scroll(up = True)

    def run(self):
        self.show_logo()


app = Application()
app.run()
