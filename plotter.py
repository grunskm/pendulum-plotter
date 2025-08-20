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

		motorY = -1 * math.sqrt(LEN**2-(self.width/2)**2)

		self.motorL = Motor(-self.width/2, motorY, board.D26, board.D19,-1, int(LEN))
		self.motorR = Motor( self.width/2, motorY, board.D20, board.D16, 1, int(LEN))
		
		pwm =  pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency = 50)
		self.pen_servo = servo.Servo(pwm)
		
		self.penUp = 160
		self.penDown = 100
		self.servoPos = self.penUp
		self.penRaise()


		
	def polarTranslate(self, X, Y, SP):
		tgtL = int(dist(self.motorL, X, Y))
		tgtR = int(dist(self.motorR, X, Y))
		self.motorR.lengthTo(tgtR,SP)
		self.motorL.lengthTo(tgtL,SP)
		self.penX = X
		self.penY = Y	

		
	def penRaise(self):
		#print("180")
		self.pen_servo.angle = 180
		time.sleep(0.25)
		#for angle in range(0, 100, 20):
			#print(angle)
			#self.pen_servo.angle = angle
			#time.sleep(1)
		
	def penLower(self):
		print("100")
		self.pen_servo.angle = 120
		time.sleep(0.25)
		#for angle in range(100, 0, -20):
			#print(angle)
			#self.pen_servo.angle = anglefrom PIL import Image
			#time.sleep(1)
	
	def line(self, X1, Y1, X2, Y2):
		self.penRaise()
		self.moveTo(X1,Y1)
		self.penLower()
		self.moveTo(X2,Y2)
		self.penRaise()
		
		#(200,200,1000,math.PI,math.TWO_PI)
		
	def semiCirc(self, X,Y,RAD,START,LEN):
		a = 0
		x=0
		y=0
		while abs(a) < abs(LEN):
			x = math.sin(a+START)*RAD+X
			y = math.cos(a+START)*RAD+Y
			self.moveTo(x,y)
			if LEN < 0:
				a -= 0.01
			else:
				a += 0.01


	
	def moveTo(self, X, Y):	
		#speed values reflect delay time; lower == faster
		max_speed = 100
		min_speed = 400
		ramp = 50
		speed = min_speed
		orig_x = self.penX
		orig_y = self.penY
	
		# calculates series of points between current and future pen position

		xDiff = float(X) - orig_x
		yDiff = float(Y) - orig_y
		
		dist = math.sqrt(xDiff**2+yDiff**2)
		if(dist == 0): return
		
		#print("distance: ", dist)
		
		xStep = float(xDiff/dist)
		yStep = float(yDiff/dist)
		
		#print("xStep: ", xStep)
		#print("yStep: ", yStep)
		
		for i in range(int(dist)):
			x = xStep * i + orig_x
			y = yStep * i + orig_y
			
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
	



