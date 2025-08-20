import time
import random
import plotter


plot = plotter.Plotter(55555, 55555)

width = 10000
height= 10000
rows = 20
cols = 20
xsep = width/cols
ysep = height/rows 
yoff = -3000

col = 0
two_pi = 6.2831

while col <= cols:
    x = col*(width/cols)-(width/2)
    y1 = 0+yoff
    y2 = -height+yoff
    
    if col%2==0:
        plot.moveTo(x,y1)
        plot.moveTo(x,y2)
        plot.semiCirc(x+xsep/2,y2,xsep/2,two_pi*0.75,-3.14)
    else:
        plot.moveTo(x,y2)
        plot.moveTo(x,y1)
        plot.semiCirc(x+xsep/2,y1,xsep/2,two_pi*0.75, 3.14)
    col+=1
    
row = 0
while row <= rows:
    x1 = -(width/2)
    x2 = width-(width/2)
    y = row*(height/rows)-(height)+yoff
    if row%2==0:
        plot.moveTo(x1,y)
        plot.moveTo(x2,y)
        plot.semiCirc(x2,y+ysep/2,ysep/2,two_pi*0.5,-3.14)
    else:
        plot.moveTo(x2,y)
        plot.moveTo(x1,y)
        plot.semiCirc(x1,y+ysep/2,ysep/2,two_pi*0.5, 3.14)
    row+=1

plot.moveTo(0,0)
print("end")
