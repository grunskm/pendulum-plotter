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

		motorY = int(math.sqrt(pow(LEN,2)-pow(SEP/2,2)))

		self.motorL = Motor(-SEP/2,-motorY, board.D26, board.D19, 1, LEN)
		self.motorR = Motor( SEP/2,-motorY, board.D20, board.D16,-1, LEN)
		
		
		
	def moveTo(self, X, Y):	
	
		#speed values reflect delay time; lower == faster
		max_speed = 100
		min_speed = 1000
		ramp = 500
		speed = min_speed
	
		# calculates series of points between current and future pen position

		xDiff = X - self.penX
		yDiff = Y - self.penY
		
		dist = math.sqrt(pow(xDiff,2)+pow(yDiff,2))/4
		if(dist == 0): return
		
		print("distance: ")
		print(dist)
		
		xStep = xDiff/dist
		yStep = yDiff/dist
		
		for i in range(int(dist)):
			x = xStep*i
			y = yStep*i
			
			if(i<ramp and i<dist/2):
				#ramp up
				speed = (math.cos(math.pi/ramp*i)*0.5+0.5)*(min_speed-max_speed)+max_speed
				
			elif(i<dist-ramp):
				#cruise
				speed = max_speed
			else:
				#ramp down
				speed = (math.cos(math.pi/ramp*(dist-i))*0.5+0.5)*(min_speed-max_speed)+max_speed

			#self.polarTranslate(x+self.penX, y+self.penY, speed)
			# print(x)
			# print(y)
		
		self.polarTranslate(X, Y, speed)	
		self.penX = X
		self.penY = Y
				

	def polarTranslate(self, X,Y,SP):
		#move each motor independently 
		#calculate distance each length needs to change
		
		tgtL = int(dist(self.motorL, X, Y))
		self.motorL.lengthTo(tgtL,SP)
		
		tgtR = int(dist(self.motorR, X, Y))
		self.motorR.lengthTo(tgtR,SP)
		

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
		
		self.length = LENGTH
		self.orientation = ORIENT
		
	
	def lengthTo(self, LEN, SPEED):
		diff = LEN - self.length
		step = 1

# 		print("moving by:")
# 		print(diff)

		#flip value of step based on motor orientation and direction
		
		if self.orientation <0:
			if diff<0:
				self.direction.value = False 
				step = -1
			else:
				self.direction.value = True 
		else:
			if diff<0:
				self.direction.value = True 
				step = -1
			else:
				self.direction.value = False 
		
# 		print("number of steps");print(diff)

		for e in range(abs(diff)):
			self.step(SPEED) 
			self.length += step
				

	def step(self, DELAY):
		# abort check?
		self.pulse.value = True
		self.pulse.value = False
		time.sleep(DELAY*0.000001)
		



    
def dist(POINT_OBJ,TGT_X,TGT_Y):
	xDiff = TGT_X-POINT_OBJ.x
	yDiff = TGT_Y-POINT_OBJ.y
	d = math.sqrt(pow(xDiff,2)+pow(yDiff,2))
	return d
	



