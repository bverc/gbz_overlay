"""Unit tests for ads1015.py
github.com/bverc/retropie-status-overlay

Author: bverc
"""

import unittest
from unittest.mock import Mock

from adc import ads1015

ads1015.adc = Mock()

class TestADS1015(unittest.TestCase):
    """A Class used to test ADC1015 module."""
    
    def mock_read_adc(self, channel, gain): 
        """A function to mock ADS1015().read_adc()"""
        if channel == 0:
            return 0
        if channel == 1:
            return 512
        return 1024

    def test_read(self):
        """Test ads1015.read()"""
        ads1015.adc.read_adc.side_effect = self.mock_read_adc
        self.assertTrue(ads1015.read(0) == 0)
        self.assertTrue(ads1015.read(1) == 1.536)
        self.assertTrue(ads1015.read(2) == 3.072)

if __name__ == '__main__':
    unittest.main()
