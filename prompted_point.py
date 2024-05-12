import time
import random
import plotter

plot = plotter.Plotter(55555, 36363)

while True:
	x = int(input("xpos: "))
	y = int(input("ypos: "))
	plot.moveTo(x,y)
	print("current pos: ")
	print(plot.penX)
	print(plot.penY)
	print("Motor Lengths: ")
	print(plot.motorL.length)
	print(plot.motorR.length)


print("end")