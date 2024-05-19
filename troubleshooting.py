import time
import random
import plotter
import random

plot = plotter.Plotter(55555, 36363)

# while True: 
	# leng = int(input("change lengths by: "))
	
	# for i in range(abs(leng)):
		# if(leng<0):
			# inc = 1
		# else:
			# inc = -1
		# plot.motorL.lengthTo(plot.motorL.length+inc, 1500)
		# plot.motorR.lengthTo(plot.motorR.length+inc, 1500)
count = 0
time.sleep(1)

while True:
	# print("Current position: ")
	# print(plot.penX)
	# print(plot.penY)
	
	# print("Left Motor Length: ")
	# print(plot.motorL.length)
	
	# print("Right Motor Length: ")
	# print(plot.motorR.length)

# 	print("move to: ")
# 	x = int(input())
# 	y = int(input())
	
# 	count += 1
# 	if count > 20:
# 		break
# 		
# 	x = random.randint(-9000,9000)
# 	y = random.randint(-9000,9000)
# 	
# 	print("moving to: ")
# 	print(x)
# 	print(y)

	plot.moveTo(x,y)
	time.sleep(1)
	plot.moveTo(0,0)
	time.sleep(1)
	
plot.moveTo(0,0)

print("end")
