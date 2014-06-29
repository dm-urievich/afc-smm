#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
#cfgfile = open('config.ini', 'r')

#config.read(cfgfile)

kp = 0.5
ki = 0.5

sections = config.sections()

if 'PID' in sections:
    try:
        kp = config.getfloat('PID', 'Kp')
    except:
        print("no args, kp")
    
    try:
        ki = config.getfloat('PID', 'Ki')
    except:
        print("no args, ki")
    
print(kp)
print(ki)

#cfgfile.close()
