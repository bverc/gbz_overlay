"""ADC Plugin for retropie-status-overlay
github.com/bverc/retropie-status-overlay

ADC module for Serial based devices, such as an Arduino

Authors: R41zan, scavenrage, bverc

Requires python module pySerial
install: python3 -m pip install pyserial

Requires serial device to be sending voltage as a string,
such as "3.61"
"""

# Import necessary library
import serial

# Setup ADC
BAUD_RATE = 9600
SERIAL_DEVICE = '/dev/ttyACM0'

try:
    ser = serial.Serial(SERIAL_DEVICE, BAUD_RATE , timeout=1)
except RuntimeError:
    pass

def read(channel): # pylint: disable=unused-argument
    """Read from ADC and return voltage."""
    ser.reset_input_buffer() # Clear input buffer
    value_v = ser.readline().decode('utf-8').rstrip()
    return float(value_v)
