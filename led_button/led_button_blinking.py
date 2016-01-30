#!/usr/bin/env python
import time as t
import RPi.GPIO as GPIO

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to on led

def blink():
	GPIO.output(LedPin, GPIO.LOW)  # Led Off
	t.sleep(0.5)
	GPIO.output(LedPin, GPIO.HIGH) # led On

def loop():
	while True:
		if GPIO.input(BtnPin) == GPIO.LOW: # Check whether the button is pressed or not.
			print '...button pressed'
			GPIO.output(LedPin, GPIO.LOW)  # Led Off
		else:
			print '...button released'
			blink()
		t.sleep(0.5)

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # Led On 
	GPIO.cleanup()                     # Cleanup resource

# main()
if __name__ == '__main__':
	setup()
	try: loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
