"""Unit tests for overlay.py
github.com/bverc/retropie-status-overlay

Author: bverc
"""

import unittest

import overlay

class TestOverlay(unittest.TestCase):
    """A Class used to test overlay module."""

    def test_get_x_pos_left(self):
        """Test get_x_pos() function from left side."""
        overlay.ICON_PADDING = "8"
        overlay.ICON_SIZE = "48"
        overlay.resolution[0] = "1920"
        overlay.config['Icons']['Horizontal'] = "left"
        count = 1
        self.assertTrue(overlay.get_x_pos(count) == 8) # 8
        count = 2
        self.assertTrue(overlay.get_x_pos(count) == 64) # 8+48+8
        count = 7
        self.assertTrue(overlay.get_x_pos(count) == 344) # ((8+48)*6)+8

    def test_get_x_pos_right(self):
        """Test get_x_pos() function from right side."""
        overlay.ICON_PADDING = "4"
        overlay.ICON_SIZE = "24"
        overlay.resolution[0] = "480"
        overlay.config['Icons']['Horizontal'] = "right"
        count = 1
        self.assertTrue(overlay.get_x_pos(count) == 452) # 480-(4+24)
        count = 2
        self.assertTrue(overlay.get_x_pos(count) == 424) # 480-2*(4+24)
        count = 7
        self.assertTrue(overlay.get_x_pos(count) == 284) # 480-7*(4+24)

if __name__ == '__main__':
    unittest.main()
