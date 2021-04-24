#!/usr/bin/env python3
########################################################################
# Filename    : LightWater.py
# Description : Use LEDBar Graph(10 LED) 
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import threading
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]
run_time=5 #Seconds of time each mode gets

def setup():    
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT)   # set all ledPins to OUTPUT mode
    GPIO.output(ledPins, GPIO.HIGH) # make all ledPins output HIGH level, turn off all led


def run_light1():
	pins1=ledPins[0:5]
	pins2=ledPins[5:10]
	zip(pins1,pins2)
	t1=time.time()
	print ('run_light1')
	while True:
		for i,j in zip(pins1, pins2):
			GPIO.output(i, GPIO.LOW)
			GPIO.output(j, GPIO.LOW)
			time.sleep(0.1)
			GPIO.output(i, GPIO.HIGH)
			GPIO.output(j, GPIO.HIGH)
		if time.time() - t1 > run_time: break

def run_light2():
        ledPinsReversed=ledPins[::-1]
        pins1=ledPins[0:10]
        pins2=ledPinsReversed[0:10]
        zip(pins1,pins2)
        t1=time.time()
        print ('run_light2')
        while True:
                for i,j in zip(pins1, pins2):
                        GPIO.output(i, GPIO.LOW)
                        GPIO.output(j, GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(j, GPIO.HIGH)
                if time.time() - t1 > run_time: break



def run_light3():
	t1=time.time()
	print('run_light3')
	while True:
		for pin in ledPins:     # make led(on) move from left to right
			GPIO.output(pin, GPIO.LOW)  
			time.sleep(0.1)
			GPIO.output(pin, GPIO.HIGH)
		if time.time() - t1 > run_time: break

def run_light4():
        pins1=ledPins[0:3]
        pins2=ledPins[3:6]
        pins3=ledPins[6:9]
        zip(pins1,pins2,pins3)
        t1=time.time()
        print ('run_light4')
        while True:
                for i,j,k in zip(pins1, pins2, pins3,):
                        GPIO.output(i, GPIO.LOW)
                        GPIO.output(j, GPIO.LOW)
                        GPIO.output(k, GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(j, GPIO.HIGH)
                        GPIO.output(k, GPIO.HIGH)
                if time.time() - t1 > run_time: break


def destroy():
    GPIO.cleanup()                     # Release all GPIO
 
if __name__ == '__main__':     # Program entrance
	print ('Program is starting...')
	setup()
	try:
		while True:
			run_light1()
			run_light2()
			run_light3()
			run_light4()
	except KeyboardInterrupt:  # Press ctrl-c to end the program.
		destroy()


