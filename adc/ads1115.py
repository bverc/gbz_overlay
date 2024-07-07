"""ADC Plugin for retropie-status-overlay
github.com/bverc/retropie-status-overlay

ADC module for Texas Instruments ADS1115 16-bit ADC
Also available as Adafruit breakout board

Authors: bverc, voxpop9

Requires ADS1115 connected via I2C, and reading on channel specified in config.ini
I2C must be enabled via raspi-config
"""

# Import necessary ADC library
import Adafruit_ADS1x15

# Setup ADC
try:
    adc = Adafruit_ADS1x15.ADS1115()
except RuntimeError:
    pass

def read(channel):
    """Read from ADC and return voltage."""
    value = adc.read_adc(channel, gain=2/3) # Channel from config.ini, 2/3 gain
    value_v = value * 0.0001875 #1 bit = 187.5uV
    return value_v
