import time
import random
import plotter

plot = plotter.Plotter(55555, 36363)


plot.moveTo(-5000,0)
time.sleep(1)

plot.moveTo(0,0)
time.sleep(1)

plot.moveTo(5000,0)
time.sleep(1)

plot.moveTo(0,0)
time.sleep(1)

plot.moveTo(0,-5000)
time.sleep(1)

plot.moveTo(0,0)
time.sleep(1)

plot.moveTo(0,5000)
time.sleep(1)

plot.moveTo(0,0)

print("end")