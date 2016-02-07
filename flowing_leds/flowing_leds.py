#!/usr/bin/env python

import time as t
import RPi.GPIO as GPIO

SER   = 11    # PIN 11 --- Input
RCLK  = 12    # PIN 12 --- Output bits to Qa-Qh
SRCLK = 13    # PIN 13 --- Input Clock

#
# Output a Knight Rider pattern
#

pattern = [
"10000000",
"01000000",
"00100000",
"00010000",
"00001000",
"00000100",
"00000010",
"00000001",
"00000010",
"00000100",
"00001000",
"00010000",
"00100000",
"01000000" ]

cleanup = "00000000"

def setup():
	GPIO.setmode(GPIO.BOARD)      # Numbers GPIOs by physical location
	GPIO.setup(SER, GPIO.OUT)     # Set SER's   mode is output
	GPIO.setup(RCLK, GPIO.OUT)    # Set RCLK's  mode is output
	GPIO.setup(SRCLK, GPIO.OUT)   # Set SRCLK's mode is input
	GPIO.output(SER, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

def writeBit(bit):
	if int(bit) == 1:
		GPIO.output(SER, GPIO.HIGH)
		GPIO.output(SRCLK, GPIO.HIGH)
	else:
		GPIO.output(SER, GPIO.LOW)
		GPIO.output(SRCLK, GPIO.HIGH)
	GPIO.output(SRCLK, GPIO.LOW)

def writeByte (byte):
	for bit in byte:
		writeBit(bit)
	GPIO.output(RCLK, GPIO.HIGH)
	GPIO.output(RCLK, GPIO.LOW)

def loop():
	while True:
		for byte in pattern:
			print byte
			writeByte(byte)
			t.sleep(0.1)
def destroy():
	# Cleanup resource
	writeByte(cleanup)
	GPIO.cleanup()

# main()
if __name__ == '__main__':
	setup()
	try: loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
