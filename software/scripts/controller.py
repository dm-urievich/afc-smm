#!/usr/bin/env python3


from optparse import OptionParser
import math
from afc_connection import readWord
from afc_connection import writeWord

signal2AmplAddr = 0
signalAmplAddr = 2
signalImagAddr = 4
signalRealAddr = 6

signal2Ampl = 0
signalAmpl = 0
signalImag = 0
signalReal = 0

kp = 0.1
ki = 0.1
out = 5632
integral = out

while True:
    # create function for readAll
    fault = readWord(signalAmplAddr)
    signal2Ampl = readWord(signal2AmplAddr)
    signalReal = readWord(signalRealAddr)
    signalImag = readWord(signalImagAddr)
    
    signalAmpl = math.sqrt(signalReal * signalReal + signalImag * signalImag)
    
    """
    print("F1Ampl = " + str(signalAmpl))
    print("F2Ampl = " + str(signal2Ampl))
    print()
    print("F1Real = " + str(signalReal))
    print("F1Imag = " + str(signalImag))
    print()
    """

    sign = 1

    if signalReal < 0:
        sign = -1

    error = signalAmpl * sign    

    integral = integral + error * ki
    out = int(integral + error * kp)
    if out > 65280:
        out = 65280

    if out < 200:
        out = 200

    print("out = " + str(out))
    writeWord(0, out)

