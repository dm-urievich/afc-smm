#!/usr/bin/env python3

import time
from optparse import OptionParser
import math
from afc_connection import readWord
from afc_connection import writeWord
from afc_connection import writeByte

kp = 6553
ki = 6553

def writePid(Kp, Ki):
    writeWord(5, Kp)
    writeWord(7, Ki)

def pidDisable():
    writeByte(9, 0)     # disable PID

def pidEnable():
    writeByte(9, 1)     # disable PID
  
def setAmpl(ampl):
    writeByte(3, ampl)    # out ampl
    
def clearAll():
    writeByte(4, 10)    # out frequency
    writeByte(3, 5)    # out ampl

    writeWord(5, kp)
    writeWord(7, ki)

    writeByte(9, 0)     # disable PID
    
    writeWord(0, 700)
    writeByte(2, 0)
    

def initFrequency():
    signal2AmplAddr = 0
    signalAmplAddr = 2
    signalImagAddr = 4
    signalRealAddr = 6

    signal2Ampl = 0
    signalAmpl = 0
    signalImag = 0
    signalReal = 0

    out = 600
    phase = 0

    writeByte(4, 10)    # out frequency
    writeByte(3, 5)    # out ampl

    writeWord(5, kp)
    writeWord(7, ki)

    writeByte(9, 0)     # disable PID

    adjCompl = False
    adjFreq = True

    imagSignCur = 0
    imagSignPrev = 0
    signalImagPrev = 0

    fault = readWord(signalAmplAddr)
    signal2Ampl = readWord(signal2AmplAddr)
    signalReal = readWord(signalRealAddr)
    signalImag = readWord(signalImagAddr)
        
    signalImagPrev = signalImag
    
    imagSignPrev  = 0
    if signalImag != 0:
        imagSignPrev = signalImag / abs(signalImag)
        
    #exit()    

    while not adjCompl:
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
        
        if signalImag != 0:
            imagSignCur = signalImag / abs(signalImag)

        if adjFreq:
            if fault == 0 and signalAmpl > 1000:
                adjFreq = False
            else:
                out = out + 100
                print ("ampl = " + str(signalAmpl))
                print("out = " + str(out))
                writeWord(0, out)
                
                if out > 65400:
                    out = 500
        else:
            if signalReal > 0:
                if imagSignCur != imagSignPrev:
                    if abs(imagSignCur) > abs(imagSignPrev):
                        if phase > 0:
                            phase = phase - 1
                        writeByte(2, phase)
                        adjCompl = True
                    else:
                        adjCompl = True
            
            if not adjCompl:
                phase = phase + 1
                print("real = " + str(signalReal))
                print("emag = " + str(signalImag))
                print("phase = " + str(phase))
                writeByte(2, phase)
                if phase == 255:
                    phase = 0
            
            signalImagPrev = signalImag
            imagSignPrev = imagSignCur
            
        time.sleep(0.1)

