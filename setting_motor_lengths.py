import time
import random
import board
import plotter

motorL = plotter.Motor(-55555/2,-55555, board.D26, board.D19, 1, 0)
motorR = plotter.Motor(55555/2,-55555, board.D20, board.D16,-1, 0)
	
count = 0

while True:
    len = input("enter length: ")
    motorR.lengthTo(len, 1000)


print("end")
