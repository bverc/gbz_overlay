"""Unit tests for adc/pj.py
github.com/bverc/retropie-status-overlay

Author: bverc
"""

import unittest

from adc import pj

class MockPiJuiceStatus(): # pylint: disable=too-few-public-methods
    """A Class to represent an pijuice.PiJuice.status()"""

    def GetBatteryVoltage(self): # pylint: disable=invalid-name, no-self-use
        """A method to mock PiJuice.status.GetBatteryVoltage()"""
        return {"data": 1100}

class TestPJ(unittest.TestCase):
    """A Class used to test PJ module."""

    def test_read(self):
        """Test pj.read()"""
        pj.pijuice.status = MockPiJuiceStatus()
        self.assertTrue(pj.read(0) == 1.1)

if __name__ == '__main__':
    unittest.main()
