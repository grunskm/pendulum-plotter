# motors mounted 45in apart at 1080 steps/inch 

import time
import math
import sys
import board
import digitalio

class Motor:
	def __init__(self, X, Y, DIR, PUL, ORT, LENGTH):
		self.x = X
		self.y = Y
		
		self.direction = digitalio.DigitalInOut(DIR)
		self.pulse = digitalio.DigitalInOut(PUL)
		
		self.direction.direction = digitalio.Direction.OUTPUT
		self.pulse.direction = digitalio.Direction.OUTPUT
		
		self.direction.value = False
		self.pulse.value = False	
		
		self.length = LENGTH
		self.orientation = ORT
		
	
	def lengthTo(self, LEN, SPEED):
		diff = math.floor(LEN - self.length)
		step = 1
# 		print("moving by:")
# 		print(diff)
		
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
		
class Canvas:
	def __init__(self, W, H):
		self.width = W
		self.height = H
		self.penX = 0
		self.penY = 0
		
	def check_sum(self, M1, M2):
		length_sum = M1.length+M2.length
		if length_sum <= self.width:
			sys.exit("motor length sums less than canvas width")
		
		
	def update_pen(self, M1, M2):
		prod = (pow(M1.length,2)+pow(self.width,2)-pow(M2.length,2))/(2*M1.length*self.width)
		ang = math.acos(prod)
		self.penX = math.cos(ang)*M1.length
		self.penY = math.sin(ang)*M1.length

canvas = Canvas(45900, 45900)
left_motor = Motor(0,0, board.D26, board.D19, 1, 36720)
right_motor = Motor(45900,0, board.D20, board.D16, -1, 36720)

def slideTo(X,Y):
		canvas.update_pen(left_motor, right_motor);

		# calculate series of points between current and future pen positions
		xDiff = X - canvas.penX
		yDiff = Y - canvas.penY
		
		dist = math.floor(math.sqrt(pow(xDiff,2)+pow(yDiff,2)))
		if(dist > 0):
		
			xStep = xDiff/dist
			yStep = yDiff/dist
		
			tempX = canvas.penX
			tempY = canvas.penY
			
			max_speed = 50
			base_speed = 1500
			speed = base_speed
			
			acc = 1.01
			limit = 0
			
			for i in range(dist):
				tempX += xStep
				tempY += yStep
				
				if(speed>max_speed and i<(dist/2)):
					speed = speed/acc
					limit = i
				elif(i>(dist-limit) and speed<base_speed):
					speed = speed*acc
# 				print(speed)
				polarTranslate(tempX, tempY,speed)
				canvas.check_sum(left_motor, right_motor);
				
			polarTranslate(X,Y,speed)
		
def polarTranslate(X,Y,SP):
	#move each motor independently 
	#calculate distance each pendulum needs to change
	
	tgt = dist(left_motor, X, Y)
	left_motor.lengthTo(tgt,SP)
	
	tgt = dist(right_motor, X, Y)
	right_motor.lengthTo(tgt,SP)
    
def dist(POINT_OBJ,TGTX,TGTY):
	xDiff = TGTX-POINT_OBJ.x
	yDiff = TGTY-POINT_OBJ.y
	d = math.sqrt(pow(xDiff,2)+pow(yDiff,2))
	return d
	
	
#----------------------- program below ----------------------------------

while True:
	canvas.update_pen(left_motor, right_motor)
	print(canvas.penX)
	print(canvas.penY)
	print("x-pos")
	x = input() 
	print("y-position")
	y = input()
	slideTo(int(x),int(y))

print("end")
