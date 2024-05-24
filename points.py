import time
import math
import random
import plotter

plot = plotter.Plotter(55555, 36363)

# n=0

# while n<10:

	# x = random.randint(-10000,10000)
	# y = random.randint(-10000,10000)

	# plot.moveTo(int(x),int(y))

	# time.sleep(1)
	# n+=1

# plot.moveTo(0,0)
while True:
	#plot.servo_val.value = True
	plot.penRaise()
	print("up")
	time.sleep(2)
	#plot.servo_val.value = False
	plot.penLower()
	print("down")
	time.sleep(2)


print("end")
