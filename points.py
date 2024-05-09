import time
import random
import plotter

plot = plotter.Plotter(55555, 36363)
n=0

while n<10:

	x = random.randint(-5000,5000)
	y = random.randint(-5000,5000)

	plot.moveTo(int(x),int(y))

	time.sleep(2)
	n+=1

plot.moveTo(0,0)

print("end")