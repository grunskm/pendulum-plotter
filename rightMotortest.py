
import random
import time
import plotter


p = plotter.Plotter(55555/2, 36363/2)

dis = 1000
delay = 1000 
wait = 0.5

while True:
	length = p.motorR.length + dis 
	p.motorL.lengthTo(length, delay)
	time.sleep(wait)
	length = p.motorR.length - dis
	p.motorL.lengthTo(length, delay)
	time.sleep(wait)

print("end")
