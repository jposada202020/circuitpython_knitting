# SPDX-FileCopyrightText: 2023 Jose D. Montoya
# SPDX-License-Identifier: MIT

"""
This example uses adafruit_display_text.label to display knitting font
icons.

"""

import board
from knitting_font import test1, test2
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

display = board.DISPLAY

font_file = "fonts/knitting-78.bdf"

# Set text, font, and color
text = "{}  {}  {}".format(test1, test2, test1)
font = bitmap_font.load_font(font_file)
color = 0xFF00FF

# Create the tet label
text_area = label.Label(font, text=text, color=color)

# Set the location
text_area.anchor_point = (0.5, 0.5)
text_area.anchored_position = (display.width // 2, display.height // 2)

# Show it
display.show(text_area)

while True:
    pass