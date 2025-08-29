import time
import random
import math
import plotter

plot = plotter.Plotter(55555, 55555)

width = 10000 
height = 15000
print(width)
print(height)
xsep = 15
#rows = 72
cols = math.floor(width/xsep)
#xsep = width/cols
#ysep = height/rows 
yoff = 1500
xoff = -width/2

col = 0
two_pi = 6.2831


try:
    while col <= cols:
        x = col*(width/cols)+xoff
        y1 = 0+yoff
        y2 = -height+yoff
      #  max_amp = xsep*0.75
        if col%2==0:
            plot.moveTo(x,y1)
            plot.moveTo(x,y2)
            plot.semiCirc(x+xsep/2,y2,xsep/2,two_pi*0.75,-3.14)
        else:
            plot.moveTo(x,y2)
            plot.moveTo(x,y1)
            plot.semiCirc(x+xsep/2,y1,xsep/2,two_pi*0.75, 3.14)
        col+=1
   #plot.moveTo(0,0)
    print("end")
    
except KeyboardInterrupt:
    plot.moveTo(0,0)
    time.sleep(2)
    print("force quit + return")
    


    
# row = 0
# while row <= rows:
    # x1 = -(width/2)
    # x2 = width-(width/2)
    # y = row*(height/rows)-(height)+yoff
    # max_amp = ysep
    # if row%2==0:
        # plot.moveTo(x1,y)
        # moveToSquig(x2,y,0)
        # plot.semiCirc(x2,y+ysep/2,ysep/2,two_pi*0.5,-3.14)
    # else:
        # plot.moveTo(x2,y)
        # moveToSquig(x1,y,0)
        # plot.semiCirc(x1,y+ysep/2,ysep/2,two_pi*0.5, 3.14)
    # row+=1

# x = 0
# print(width)
# while x < width:
    # x += 0.1
    # print(x)
    # freq = 0.05
    # speed = 500
    
    # af = 100
    # a = 0
    # amp = 0
    
    # while a<af:
        # xx = (x/width*(img.width-af))+a
        # yy = 500
        # coord = xx,yy
        # amp += 100-(img.getpixel(coord)[0]/255*100)
        # a+=1
    
    # amp = amp/af
        
    # x_mod = math.sin(x*freq)*amp
    # plot.polarTranslate(x_mod, 0, speed)



    

    
            
