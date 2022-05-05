# ADC Plugin for retropie-status-overlay
# github.com/bverc/retropie-status-overlay
#
# ADC module for PiSugar3
# https://github.com/PiSugar/PiSugar/wiki/PiSugar-3-Series
#
# Author: bverc
#
# I2C must be enabled via raspi-config

# Import smbus for I2C interface
import smbus

#  PiSugar register is at address 0x57
address = 0x57

# Initialize I2C (SMBus) on I2C Channel 1
bus = smbus.SMBus(1)

# ADC read function, return voltage
def read(channel):
  return bus.read_word_data(address, 0x22) / 1000
