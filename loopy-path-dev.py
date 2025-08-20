import time
import random
import math
import plotter


plot = plotter.Plotter(55555,55555)

width = 10000
height = 10000

def lerp(N1,N2,T):
    return N1+(N2-N1)*T

def randx():
    return random.randint(-width/2,width/2)

def randy():
    return random.randint(-height,0)

try:
    e = 0

    x1 = randx()
    y1 = randy()
    x2 = randx()
    y2 = randy()
    x3 = randx()
    y3 = randy()
    x4 = randx()
    y4 = randy()

    while e<10:
        e = e+1
        t = 0
        while t<1:
            t = t+0.001
            dx1 = lerp(x1,x2,t)
            dy1 = lerp(y1,y2,t)
            dx2 = lerp(x2,x3,t)
            dy2 = lerp(y2,y3,t)
            dx3 = lerp(x3,x4,t)
            dy3 = lerp(y3,y4,t)
            px1 = lerp(dx1,dx2,t)
            py1 = lerp(dy1,dy2,t)
            px2 = lerp(dx2,dx3,t)
            py2 = lerp(dy2,dy3,t)
            x = lerp(px1,px2,t)
            y = lerp(py1,py2,t)
            plot.moveTo(x,y)
        
        x1 = x4
        y1 = y4
        x2 = x4-(x3-x4)
        y2 = y4-(y3-y4)
        x3 = randx()
        y3 = randy()
        x4 = randx()
        y4 = randy()
    plot.moveTo(0,0)

except KeyboardInterrupt:
    plot.moveTo(0,0)

