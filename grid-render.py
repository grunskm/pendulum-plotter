import time
import random
import math
import plotter
from PIL import Image

img = Image.open("images/rust_02.jpg")
print(img.height)
print(img.width)

plot = plotter.Plotter(55555, 55555)
scale = 5
width = img.width*scale
height = img.height*scale
print(width)
print(height)
xsep = 75
#rows = 72
cols = math.floor(width/xsep)
#xsep = width/cols
#ysep = height/rows 
yoff = 0
xoff = -width/2
max_amp = xsep

col = 0
two_pi = 6.2831

def map_range(SRC,SRC_MIN,SRC_MAX,OUT_MIN,OUT_MAX):
    return (SRC/(SRC_MIN-SRC_MAX)*(OUT_MIN-OUT_MAX))+OUT_MIN

def moveToSquig(X, Y, DIR):	
    global img
    global height
    global width
    global max_amp
    orig_x = plot.penX
    orig_y = plot.penY

    xDiff = float(X) - orig_x
    yDiff = float(Y) - orig_y
    
    dist = math.sqrt(xDiff**2+yDiff**2)
    if(dist == 0): return
    
    xStep = float(xDiff/dist)
    yStep = float(yDiff/dist)

    for i in range(int(dist)):
        tx = xStep * i + orig_x
        ty = yStep * i + orig_y
        # xx = x/width*(img.width-af)
        # yy = y/height*(img.height-af)
        d = math.floor(max_amp*0.25)
        af = d*d
        a = 0
        amp = 0
        freq = 0.25
        while a<af:
            xx = math.floor((tx-xoff)/width*(img.width-d))+(a%d)
            yy = math.floor((ty-yoff)/height*(img.height-d))+(math.floor(a/d))
            coord = xx,yy
            amp += img.getpixel(coord)[0]
            a+=1
        amp = max_amp-(amp/af/255)*max_amp
        #amp = map_range(pow(amp,2),0,max_amp*max_amp,0,max_amp)
        #print(amp)
        #freq = map_range(amp,0,max_amp,0.001,0.01)
        
        mod_x = 0
        mod_y = 0
        
        if(DIR == 0): 
            mod_y = math.sin(tx*freq)*amp
        else: 
            mod_x = math.sin(ty*freq)*amp
        
        #speed = 400+amp
        plot.moveTo(tx+mod_x, ty+mod_y)

    
    plot.moveTo(X, Y)	


try:
    while col <= cols:
        x = col*(width/cols)+xoff
        y1 = 0+yoff
        y2 = -height+yoff
      #  max_amp = xsep*0.75
        if col%2==0:
            plot.moveTo(x,y1)
            moveToSquig(x,y2,1)
            plot.semiCirc(x+xsep/2,y2,xsep/2,two_pi*0.75,-3.14)
        else:
            plot.moveTo(x,y2)
            moveToSquig(x,y1,1)
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



    

    
            
