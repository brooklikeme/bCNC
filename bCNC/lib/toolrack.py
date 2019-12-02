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

DEFAULT_DELAY = 0.001
PREPARE_OFFSET = 4.3 # mm from init position
EXEC_DISTANCE = 1.3

ATC_UN_INIT = 0
ATC_LOOSEING = 1
ATC_CLAMPING = 2


class ToolRack(object):

    ATCStatus = ATC_UN_INIT

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
        while GPIO.input(GPIO_LIMIT):
            self.ATCUp(DEFAULT_DELAY, SPM * 0.01) # atc up until limit switch is triggered
        # go down
        self.ATCDown(DEFAULT_DELAY, SPM * PREPARE_OFFSET)
        self.ATCStatus = ATC_CLAMPING

    def execClampTool(self):
        if self.ATCStatus == ATC_UN_INIT:
            self.initATC()
        elif self.ATCStatus == ATC_CLAMPING:
            return
        print('execClampTool!')
        self.ATCUp(DEFAULT_DELAY, SPM * EXEC_DISTANCE)
        self.ATCStatus = ATC_CLAMPING

    def execLooseTool(self):
        if self.ATCStatus == ATC_UN_INIT:
            self.initATC()
        elif self.ATCStatus == ATC_LOOSEING:
            return
        print('execLooseTool!')
        self.ATCDown(DEFAULT_DELAY, SPM * EXEC_DISTANCE)
        self.ATCStatus = ATC_LOOSEING

