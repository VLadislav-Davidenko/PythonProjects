def KelvinToFahrenheir(temp):
	assert (temp >= 0), "Coldest than absolute zero"
	return ((temp - 273) * 1.8 ) + 32
print (KelvinToFahrenheir(34))
print (round(KelvinToFahrenheir(451), 2))
try:
	print (KelvinToFahrenheir(-12))
except AssertionError:   
	print("It can't be coldest than absolute zero")
else:
	print("Passed")
	print(KelvinToFahrenheir(-12))

try:
	print(KelvinToFahrenheir(123))
finally:
	print("Error, it can't be so")