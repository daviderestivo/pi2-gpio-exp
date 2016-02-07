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
"01000000"
]

def setup():
	GPIO.setmode(GPIO.BOARD)      # Numbers GPIOs by physical location
	GPIO.setup(SER, GPIO.OUT)     # Set SER's   mode is output
	GPIO.setup(RCLK, GPIO.IN)     # Set RCLK's mode is output
	GPIO.setup(SRCLK, GPIO.IN)    # Set SRCLK's mode is input

def writeBit(bit):
	# Wait for the serial clock to go from LOW to HIGH
	while GPIO.input(SRCLK) == GPIO.LOW:
		pass
	if int(bit) == 1:
		GPIO.output(SER, GPIO.HIGH)
	else:
		GPIO.output(SER, GPIO.LOW)

def writeByte (byte):
	for bit in byte:
		writeBit(bit)
	GPIO.output(RCLK, GPIO.HIGH)

def loop():
	while True:
		for byte in pattern:
			writeByte(byte)
			t.sleep(0.2)

def destroy():
	GPIO.cleanup()                     # Cleanup resource

# main()
if __name__ == '__main__':
	setup()
	try: loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
