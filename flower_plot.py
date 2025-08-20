import time
import random
import math
import plotter
import json

with open('flower_data/00_angela.json','r') as f:
    flower = json.load(f)
    print(flower)
    print(flower["name"])
    print(flower["coords"])

plot = plotter.Plotter(55555,55555)

width = 1000
height = 1000 

def draw_flower(FLOWER):
    coord = FLOWER["coords"]
    i = 0

    while i < len(coord):
        i = i+1
        x = coord[i]["x"]*10
        y = coord[i]["y"]*-10
        if x > 0:
            plot.moveTo(x,y)

try:
    draw_flower(flower)
  #  e = 0
   # while e<10:
    #    e = e+1
     #   t = 0
      #  while f<flower:
       #     f = f+1
        #    plot.moveTo(x,y)

    plot.moveTo(0,0)

except KeyboardInterrupt:
    plot.moveTo(0,0)

