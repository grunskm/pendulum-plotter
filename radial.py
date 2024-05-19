import time
import math
import random
import plotter

plot = plotter.Plotter(55555, 36363)

count = 0
i = 0
while i<60:
    deg = i * (math.pi/60*2)
    x = math.sin(deg)*3000
    y = math.cos(deg)*3000
    plot.moveTo(x,y)
    time.sleep(0.5)
    if (i % 2) != 0 :
        plot.moveTo(0,0)
        time.sleep(0.5)
    i+=1

plot.moveTo(0,0)

