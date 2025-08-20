import time
import random
import math
import plotter
from PIL import Image

plot = plotter.Plotter(55555, 55555)

try:
    rows = 15
    cols = 15
    space = 2000
    col = 0
    while col <= cols:
        x = col*space-(space*rows/2)
        y1 = 0
        y2 = -cols*space
        if col%2==0:
            plot.moveTo(x,y1)
            plot.moveTo(x,y2)
        else:
            plot.moveTo(x,y2)
            plot.moveTo(x,y1)
        col+=1
    
    row = 0
    while row <= rows:
        y = -row*space
        x1 = -space*rows/2
        x2 = rows*space/2
        if row%2==0:
            plot.moveTo(x1,y)
            plot.moveTo(x2,y)
        else:
            plot.moveTo(x2,y)
            plot.moveTo(x1,y)
        row+=1
    print("end")
    plot.moveTo(0,0)
    
except KeyboardInterrupt:
    plot.moveTo(0,0)
    time.sleep(2)
    print("force quit + return")
    
