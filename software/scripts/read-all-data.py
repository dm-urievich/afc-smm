#!/usr/bin/env python3

import struct
from optparse import OptionParser

import serial

signal2AmplAddr = 0
signalAmplAddr = 2
signalImagAddr = 4
signalRealAddr = 6

signal2Ampl = 0
signalAmpl = 0
signalImag = 0
signalReal = 0

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None)

def readWord(addr):
    command = 0b00010000
    binData = struct.pack('>BBHB', 0, command, addr, 2)
    ser.write(binData)
    data = ser.read(2)
    return int.from_bytes(data, byteorder='big', signed=True)

# create function for readAll
signalAmpl = readWord(signalAmplAddr)
signal2Ampl = readWord(signal2AmplAddr)
signalReal = readWord(signalRealAddr)
signalImag = readWord(signalImagAddr)

print("F1Ampl = " + str(signalAmpl))
print("F2Ampl = " + str(signal2Ampl))
print()
print("F1Real = " + str(signalReal))
print("F1Imag = " + str(signalImag))
print()

ser.close()
