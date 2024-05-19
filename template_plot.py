
import random
import plotter


p = plotter.Plotter(30000, 20000)

d = 5000

while True:
	length = p.motorR.length + d 
	p.motorR.lengthTo(length, 1000)
	length = p.motorR.length - d 
	p.motorR.lengthTo(length, 1000)

print("end")
