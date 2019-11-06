# -*- coding: ascii -*-
# $Id$
#
# Author: zhangqx2008@gmail.com
# Date: 18-Jun-2019


try:
	import RPi.GPIO as GPIO
except ImportError:
	from fakerpi import GPIO as GPIO

from time import sleep


GPIO_STEP = 17   # Direction GPIO Pin
GPIO_DIR = 27  # Step GPIO Pin
GPIO_LIMIT = 22 # ATC Switch Pin
SPM = 518   # Steps per mm (200 * 5.18 / 2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_STEP, GPIO.OUT) # GPIO Assign mode
GPIO.setup(GPIO_DIR, GPIO.OUT) # GPIO Assign mode
GPIO.setup(GPIO_LIMIT, GPIO.IN) # GPIO Assign mode

DEFAULT_DELAY = 0.005
PREPARE_OFFSET = 1 # mm from init position
EXEC_DISTANCE = 1


class ToolRack(object):
    def __init__(self):
        return

    def execSteps(self, delay, steps):
        steps = int(steps)
        for x in range(steps):
            GPIO.output(GPIO_STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(GPIO_STEP, GPIO.LOW)
            sleep(delay)

    def ATCUp(self, delay, steps):
        GPIO.output(GPIO_DIR, 1)
        self.execSteps(delay, steps)

    def ATCDown(self, delay, steps):
        GPIO.output(GPIO_DIR, 0)
        self.execSteps(delay, steps)

    def initATC(self):
        if GPIO.input(GPIO_LIMIT):
            print('triggered!')
        else:
            print('not triggered!')
        return
        #while not GPIO.input(GPIO_LIMIT):
        #    self.ATCUp(DEFAULT_DELAY, SPM / 10) # atc up until limit switch is triggered
        # go down
        #self.ATCDown(DEFAULT_DELAY, SPM * PREPARE_OFFSET)

    def execClampTool(self):
        print('execClampTool!')
        self.ATCUp(DEFAULT_DELAY, SPM * EXEC_DISTANCE)

    def execLooseTool(self):
        print('execLooseTool!')
        self.ATCDown(DEFAULT_DELAY, SPM * EXEC_DISTANCE)

