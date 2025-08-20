import time
import random
import math
import plotter
from PIL import Image

img = Image.open("checker.jpg")
print(img.height)
print(img.width)

plot = plotter.Plotter(55555, 55555)

width = 10000
height= 10000
xsep = 100 
#rows = 72
cols = math.floor(width/xsep)
#xsep = width/cols
#ysep = height/rows 
yoff = -height-5000
xoff = -width/2
max_amp = xsep

col = 0
two_pi = 6.2831

def map_range(SRC,SRC_MIN,SRC_MAX,OUT_MIN,OUT_MAX):
    return (SRC/(SRC_MIN-SRC_MAX)*(OUT_MIN-OUT_MAX))+OUT_MIN

def moveToSquig(X, Y):	
    global img
    global height
    global width
    global max_amp
    orig_x = plot.penX - xoff
    orig_y = plot.penY - yoff

    xDiff = float(X) - orig_x 
    yDiff = float(Y) - orig_y 
    
    dist = math.sqrt(xDiff**2+yDiff**2)
    if(dist == 0): return
    
    xStep = float(xDiff/dist)
    yStep = float(yDiff/dist)

    for i in range(int(dist)):
        tx = xStep * i + orig_x
        ty = yStep * i + orig_y

        af = 25
        a = 0
        amp = 0
        freq = 0.1
        while a<af:
            xx = tx/width*(200)+(a%5)+300 
            yy = ty/height*(200)+(math.floor(a/5))+200
            coord = xx,yy
            amp += max_amp-(img.getpixel(coord)[0]/255*max_amp)
            a+=1
        amp = amp/af
        #amp = map_range(pow(amp,2),0,max_amp*max_amp,0,max_amp)
        #print(amp)
        #freq = map_range(amp,0,max_amp,0.001,0.01)
        
        mod = math.sin(i*freq)*amp
        
        d = math.sqrt( i**2 + mod**2 )
        a = math.atan2(i,mod)-math.atan2(tx-orig_x,ty-orig_y)

        rot_x = math.cos(a)*d+orig_x
        rot_y = math.sin(a)*d+orig_y

        plot.moveTo(rot_x+xoff, rot_y+yoff)

    #plot.moveTo(X, Y+yoff)	



try:
    
    d_space = 142
    lines = height/d_space
    line = 0

    while line <= lines:
        x1 = line*d_space
        y1 = 0
        x2 = 0
        y2 = line*d_space
        
        if line%2==0:
            plot.moveTo(x1+xoff,y1+yoff)
            moveToSquig(x2,y2)
            #plot.semiCirc(x+xsep/2,y2,xsep/2,two_pi*0.75,-3.14)
        else:
            plot.moveTo(x2+xoff,y2+yoff)
            moveToSquig(x1,y1)
            #plot.semiCirc(x+xsep/2,y1,xsep/2,two_pi*0.75, 3.14)
        line+=1
    
    line = 0
    while line <= lines:
        x1 = line*d_space
        y1 = height
        x2 = width
        y2 = line*d_space
         
        if line%2==0:
            plot.moveTo(x1+xoff,y1+yoff)
            moveToSquig(x2,y2)
            #plot.semiCirc(x+xsep/2,y2,xsep/2,two_pi*0.75,-3.14)
        else:
            plot.moveTo(x2+xoff,y2+yoff)
            moveToSquig(x1,y1)
            #plot.semiCirc(x+xsep/2,y1,xsep/2,two_pi*0.75, 3.14)
        line+=1

    # while line <= lines:
        # x1 = line*d_space
        # y1 = height
        # x2 = 0
        # y2 = height - (line*d_space)
         
        # if line%2==0:
            # plot.moveTo(x1+xoff,y1+yoff)
            # moveToSquig(x2,y2)
            # #plot.semiCirc(x+xsep/2,y2,xsep/2,two_pi*0.75,-3.14)
        # else:
            # plot.moveTo(x2+xoff,y2+yoff)
            # moveToSquig(x1,y1)
            # #plot.semiCirc(x+xsep/2,y1,xsep/2,two_pi*0.75, 3.14)
        # line+=1
    
    # line = 0
    # while line <= lines:
        # x1 = line*d_space
        # y1 = 0
        # x2 = width
        # y2 = height-line*d_space
         
        # if line%2==0:
            # plot.moveTo(x1+xoff,y1+yoff)
            # moveToSquig(x2,y2)
            # #plot.semiCirc(x+xsep/2,y2,xsep/2,two_pi*0.75,-3.14)
        # else:
            # plot.moveTo(x2+xoff,y2+yoff)
            # moveToSquig(x1,y1)
            # #plot.semiCirc(x+xsep/2,y1,xsep/2,two_pi*0.75, 3.14)
        # line+=1

    plot.moveTo(0,0)
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



    

    
            
