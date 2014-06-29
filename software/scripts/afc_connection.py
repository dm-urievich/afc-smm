
import struct
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
try:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None)
except:
    print("connect serial port!")

def readWord(addr):
    command = 0b00010000
    binData = struct.pack('>BBHB', 0, command, addr, 2)
    ser.write(binData)
    data = ser.read(2)
    return int.from_bytes(data, byteorder='big', signed=True)

def writeWord(addr, data):
    command = 0b00100000
    binData = struct.pack('>BBHBH', 0, command, addr, 2, data)
    ser.write(binData)

def writeByte(addr, data):
    command = 0b00100010
    binData = struct.pack('>BBHBB', 0, command, addr, 1, data)
    ser.write(binData)