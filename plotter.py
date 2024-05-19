# motors mounted 55in apart at 1080 steps/inch (currently 1010 steps/in) 

# ideas to test accuracy:
# use base functions independently + record position

import time
import math
import sys
import digitalio
import board


class Plotter:
	def __init__(self, SEP, LEN):

		self.penX = 0
		self.penY = 0
		self.width = int(SEP)

		motorY = math.sqrt(LEN**2-(self.width/2)**2)

		self.motorL = Motor(-self.width/2,-motorY, board.D26, board.D19, 1, int(LEN))
		self.motorR = Motor( self.width/2,-motorY, board.D20, board.D16,-1, int(LEN))
		
	def polarTranslate(self, X, Y, SP):
		tgtL = int(dist(self.motorL, X, Y))
		tgtR = int(dist(self.motorR, X, Y))
		self.motorR.lengthTo(tgtR,SP)
		self.motorL.lengthTo(tgtL,SP)
		
	def moveTo(self, X, Y):	
	
		#speed values reflect delay time; lower == faster
		max_speed = 100
		min_speed = 1400
		ramp = 300
		speed = min_speed
	
		# calculates series of points between current and future pen position

		xDiff = float(X) - self.penX
		yDiff = float(Y) - self.penY
		
		dist = math.sqrt(xDiff**2+yDiff**2)
		if(dist == 0): return
		
		print("distance: ", dist)
		
		xStep = float(xDiff/dist)
		yStep = float(yDiff/dist)
		
		print("xStep: ", xStep)
		print("yStep: ", yStep)
		
		for i in range(int(dist)):
			x = xStep * i + self.penX
			y = yStep * i + self.penY
			
			if i<ramp and i<dist/2:
				#ramp up
				speed = (math.cos(math.pi/ramp*i)*0.5+0.5)*(min_speed-max_speed)+max_speed
				
			elif i<dist-ramp:
				#cruise
				speed = max_speed
			else:
				#ramp down
				speed = (math.cos(math.pi/ramp*(dist-i))*0.5+0.5)*(min_speed-max_speed)+max_speed

			self.polarTranslate(x, y, speed)
			# print(x)
			# print(y)
		
		self.polarTranslate(X, Y, speed)	
		self.penX = X
		self.penY = Y
		
	 
		



		
class Motor:
	def __init__(self, X, Y, DIR, PUL, ORIENT, LENGTH):
		self.x = X
		self.y = Y
		
		self.direction = digitalio.DigitalInOut(DIR)
		self.pulse = digitalio.DigitalInOut(PUL)
		
		self.direction.direction = digitalio.Direction.OUTPUT
		self.pulse.direction = digitalio.Direction.OUTPUT
		
		self.direction.value = False
		self.pulse.value = False	
		
		self.length = int(LENGTH)
		self.orientation = ORIENT
		
	
	def lengthTo(self, LEN, SPEED):
		diff = int(LEN) - self.length 
		step = 1

		#print("moving by: ", diff)


		#flip value of step based on motor orientation and direction
		
		if self.orientation < 0:
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

		for e in range(diff):
			self.step(SPEED) 
			self.length += step
			
		# while self.length != LEN:
			# self.step(SPEED)
			# self.length += step
				
	def step(self, DELAY):
		# abort check?
		self.pulse.value = True
		time.sleep(DELAY*0.000001)
		self.pulse.value = False
		time.sleep(DELAY*0.000001)
		



    
def dist(POINT_OBJ,TGT_X,TGT_Y):
	xDiff = float(TGT_X)-POINT_OBJ.x
	yDiff = float(TGT_Y)-POINT_OBJ.y
	d = math.sqrt(xDiff**2+yDiff**2)
	return d
	



