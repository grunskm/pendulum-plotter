import time
import math
import random
import plotter

plot = plotter.Plotter(55555, 36363)

n = 0

while n<10:
	x1 = random.randint(-10000,10000)
	y1 = random.randint(-10000,10000)
	x2 = random.randint(-10000,10000)
	y2 = random.randint(-10000,10000)

	plot.line(int(x1),int(y1),int(x2),int(y2))

	n+=1

# plot.moveTo(0,0)

# while True:
	# plot.penRaise()
	# time.sleep(2)
	# plot.penLower()
	# time.sleep(2)

# while True:
	# ang = input("servo angle: ")
	# plot.pen_servo.angle = int(ang)
	

plot.moveTo(0,0)

print("end")
