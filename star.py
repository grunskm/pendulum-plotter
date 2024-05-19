import time
import random
import plotter

plot = plotter.Plotter(55555/2, 36363/2)

width = 8000/2
divs = 9

for i in range(divs):
    x = (width/divs*i)-(width/2)
    y = -width/2
    plot.moveTo(x,y)
    time.sleep(1)
    plot.moveTo(0,0)
    time.sleep(1)
    
for i in range(divs):
    x = width/2
    y = (width/divs*i)-(width/2)
    plot.moveTo(x,y)
    time.sleep(1)
    plot.moveTo(0,0)
    time.sleep(1)
    
for i in range(divs):
    x = width-(width/divs*i)-(width/2)
    y = width/2
    plot.moveTo(x,y)
    time.sleep(1)
    plot.moveTo(0,0)
    time.sleep(1)

for i in range(divs):
    y = width-(width/divs*i)-(width/2)
    x = width/2
    plot.moveTo(x,y)
    time.sleep(1)
    plot.moveTo(0,0)
    time.sleep(1)

plot.moveTo(0,0)
print("end")
