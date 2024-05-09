# motors mounted 55in apart at 1080 steps/inch (currently 1010 steps/in) 

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
		
		dist = math.floor(math.sqrt(pow(xDiff,2)+pow(yDiff,2)))
		if(dist > 0):
		
			xStep = xDiff/dist
			yStep = yDiff/dist
			
			#speed values reflect delay time; lower == faster
			max_speed = 50
			base_speed = 1500
			speed = base_speed
			
			acc = 1.01
			limit = 0
			
			for i in range(dist):
				self.penX += xStep
				self.penY += yStep
				
				if(speed>max_speed and i<(dist/2)):
					speed = speed/acc
					limit = i
				elif(i>(dist-limit) and speed<base_speed):
					speed = speed*acc
					
				self.polarTranslate(self.penX, self.penY,speed)
				
			self.penX = X
			self.penY = Y
			
			self.polarTranslate(self.penX,self.penY,speed)

				

	def polarTranslate(self, X,Y,SP):
		#move each motor independently 
		#calculate distance each length needs to change
		
		tgt = dist(self.motorL, X, Y)
		self.motorL.lengthTo(tgt,SP)
		
		tgt = dist(self.motorR, X, Y)
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
		



    
def dist(POINT_OBJ,TGT_X,TGT_Y):
	xDiff = TGT_X-POINT_OBJ.x
	yDiff = TGT_Y-POINT_OBJ.y
	d = math.sqrt(pow(xDiff,2)+pow(yDiff,2))
	return d
	



