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
		self.width = SEP

		motorY = math.sqrt(pow(LEN,2)-pow(SEP/2,2))

		self.motorL = Motor(-SEP/2,-motorY, board.D26, board.D19, 1, LEN)
		self.motorR = Motor( SEP/2,-motorY, board.D20, board.D16,-1, LEN)
		
		
	def moveTo(self, X, Y):
		# calculates series of points between current and future pen position

		xDiff = X - self.penX
		yDiff = Y - self.penY
		
		dist = int(math.sqrt(pow(xDiff,2)+pow(yDiff,2)))
	
		xStep = xDiff/dist
		yStep = yDiff/dist
		
		#speed values reflect delay time; lower == faster
		max_speed = 50
		min_speed = 1500
		ramp = 5000
		
		for i in range(dist):
			self.penX += xStep
			self.penY += yStep
			
			if(i<ramp and i<dist/2):
				#ramp up
				speed = (cos(PI/ramp*i)*0.5+0.5)*(min_speed-max_speed)+max_speed
				
			elif(i<dist-ramp):
				#cruise
				speed = max_speed
			else:
				#ramp down
				speed = (cos(PI/ramp*(dist-i))*0.5+0.5)*(min_speed-max_speed)+max_speed

			self.polarTranslate(self.penX, self.penY, speed)
				
# 			self.penX = X
# 			self.penY = Y
# 			
# 			self.polarTranslate(self.penX,self.penY,speed)

				

	def polarTranslate(self, X,Y,SP):
		#move each motor independently 
		#calculate distance each length needs to change
		
		tgt = int(dist(self.motorL, X, Y))
		self.motorL.lengthTo(tgt,SP)
		
		tgt = int(dist(self.motorR, X, Y))
		self.motorR.lengthTo(tgt,SP)
		

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
				

	def step(self, DELAY):
		self.pulse.value = True
		self.pulse.value = False
		time.sleep(DELAY*0.000001)
		



    
def dist(POINT_OBJ,TGT_X,TGT_Y):
	xDiff = TGT_X-POINT_OBJ.x
	yDiff = TGT_Y-POINT_OBJ.y
	d = math.sqrt(pow(xDiff,2)+pow(yDiff,2))
	return d
	



