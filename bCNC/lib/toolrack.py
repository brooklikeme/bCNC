# -*- coding: ascii -*-
# $Id$
#
# Author: zhangqx2008@gmail.com
# Date: 18-Jun-2019


try:
	import RPi.GPIO as GPIO
except ImportError:
	from fakerpi import GPIO as GPIO

GPIO_TOOLRACK = 17

GPIO_AIRPUMP  = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TOOLRACK, GPIO.OUT, initial=GPIO.HIGH) # GPIO Assign mode
GPIO.setup(GPIO_AIRPUMP, GPIO.OUT, initial=GPIO.HIGH) # GPIO Assign mode

class ToolRack(object):
    def __init__(self):
        return

    def enableToolRack(self):
        print('Tool rack enabled!')
        GPIO.output(GPIO_TOOLRACK, GPIO.LOW)

    def disableToolRack(self):
        print('Tool rack disabled!')
        GPIO.output(GPIO_TOOLRACK, GPIO.HIGH)

    def openAirPump(self):
        print('AirPump opend!')
        GPIO.output(GPIO_AIRPUMP, GPIO.LOW)

    def closeAirPump(self):
        print('AirPump closed!')
        GPIO.output(GPIO_AIRPUMP, GPIO.HIGH)

