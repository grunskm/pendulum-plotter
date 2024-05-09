
import time
import math
import sys
import digitalio
import board

from pynput import keyboard

class Motor:
	def __init__(self, DIR, PUL, ORIENT):

		
		self.direction = digitalio.DigitalInOut(DIR)
		self.pulse = digitalio.DigitalInOut(PUL)
		
		self.direction.direction = digitalio.Direction.OUTPUT
		self.pulse.direction = digitalio.Direction.OUTPUT
		
		self.direction.value = False
		self.pulse.value = False	
		
		self.orientation = ORIENT
		
	
	def lengthTo(self, LEN, SPEED):
		diff = math.floor(LEN - self.length)
		step = 1

# 		print("moving by:")
# 		print(diff)

		#flip value of step based on motor orientation and direction
		
		if self.orientation <0:
			if diff<0:
				self.direction.value = False 
				diff *= -1
				step = -1
			else:
				self.direction.value = True 
		else:
			if diff<0:
				self.direction.value = True 
				diff *= -1
				step = -1
			else:
				self.direction.value = False 
		
# 		print("number of steps");print(diff)
		if diff>1:
			for e in range(diff):
				self.step(SPEED) 
				self.length += step
				

	def step(self, DELAY):
		self.pulse.value = True
		self.pulse.value = False
		time.sleep(DELAY*0.000001)

motorL = Motor( board.D26, board.D19, 1)
motorR = Motor( board.D20, board.D16, 1)

distance = 0

while True:
	len = input("enter length")
	print("len: ");print(len)

	for i in range(int(len)):
		motorL.step(1000)
		motorR.step(1000)
		print(i)
		distance += 1
	print("distance: ");print(distance)	 






	

