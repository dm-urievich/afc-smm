#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
#config.read('config.ini')
cfgfile = open('config.ini', 'w')

config.add_section('PORT')

config.add_section('SIGNAL')

config.add_section('PID')
config.set('PID', 'Kp', '0.1')
config.set('PID', 'Ki', '0.1')
config.write(cfgfile)

cfgfile.close()

