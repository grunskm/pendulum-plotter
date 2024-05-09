
import random
import plotter


p = plotter.Plotter(30000, 20000)

while True:
	print(p.penX)
	print(p.penY)
	print("x-pos")
	x = random.randint(-10000,10000)
	print("y-position")
	y = random.randint(-10000,10000)
	p.moveTo(int(x),int(y))

print("end")