import math

def square_area_to_circle(size):
	r = math.sqrt(size)/2
	return (r ** 2)  * math.pi
	#return size * math.pi / 4.0
print(square_area_to_circle(9))