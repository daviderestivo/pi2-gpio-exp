#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

SDI   = 11
RCLK  = 12
SRCLK = 13
countdown = 60 # 60 Seconds countdown

segmentCodes = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

def print_msg():
	print 'Timer started ... 60 seconds countdown'
	print 'Please press Ctrl+C to end the program...'

def setup():
	GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

def write_digit(num):
	for bit in range(0, 8):	
		GPIO.output(SDI, 0x80 & (num << bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(SRCLK, GPIO.LOW)
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(RCLK, GPIO.LOW)

def loop():
	while True:
		for i in range(countdown, -1, -1):
			write_digit(segmentCodes[i%10])
			write_digit(segmentCodes[i/10])
			time.sleep(1.0)

def destroy():   # When program ending, the function is executed. 
	GPIO.cleanup()

if __name__ == '__main__': #Program starting from here 
	print_msg()
	setup() 
	try:
		loop()  
	except KeyboardInterrupt:  
		destroy()  

