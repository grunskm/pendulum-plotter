# motors mounted 55in apart at 1080 steps/inch (currently 1010 steps/in) 

import time
import math
import sys
import digitalio
import pwmio
import board
from adafruit_motor import servo


class Plotter:
	def __init__(self, SEP, LEN):

		self.penX = 0
		self.penY = 0
		self.width = int(SEP)
		self.penUp = 0
		self.penDown = 50

		motorY = math.sqrt(LEN**2-(self.width/2)**2)

		self.motorL = Motor(-self.width/2,-motorY, board.D26, board.D19, 1, int(LEN))
		self.motorR = Motor( self.width/2,-motorY, board.D20, board.D16,-1, int(LEN))
		
		pwm =  pwmio.PWMOut(board.D12, duty_cycle=2**15, frequency = 50)
		self.pen_servo = servo.Servo(pwm)
		self.penRaise()
		# self.servo_val = digitalio.DigitalInOut(board.D12)
		# self.servo_val.direction = digitalio.Direction.OUTPUT
		
	def polarTranslate(self, X, Y, SP):
		tgtL = int(dist(self.motorL, X, Y))
		tgtR = int(dist(self.motorR, X, Y))
		self.motorR.lengthTo(tgtR,SP)
		self.motorL.lengthTo(tgtL,SP)
		
	def penRaise(self):
		print("pen down")
		
		self.pen_servo.angle = 0
		
		#p1 = self.penDown
		#p2 = self.penUp
		#for angle in range(0, p2, 5):
		#	self.pen_servo.angle = angle
		#	time.sleep(0.05)
		
	def penLower(self):
		print("pen up")
		self.pen_servo.angle = 90
		# p1 = self.penUp
		# p2 = self.penDown
		# for angle in range(p1, p2, -5):
			# self.pen_servo.angle = angle
			# time.sleep(0.05)
	
	def moveTo(self, X, Y):	
		#speed values reflect delay time; lower == faster
		max_speed = 100
		min_speed = 700
		ramp = 500
		speed = min_speedD12
	
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
	



