import time
import random
import plotter

plot = plotter.Plotter(55555, 36363)

count = 0

while True:
    count += 1
    if count > 50: break
    
    k = count*100
    
    plot.moveTo(-k,k)
    time.sleep(1)

    plot.moveTo(k,k)
    time.sleep(1)

    plot.moveTo(k,-k)
    time.sleep(1)

    plot.moveTo(-k,-k)
    time.sleep(1)
    
    plot.moveTo(-k,k)
    time.sleep(1)

plot.moveTo(0,0)
print("end")