def dbl_linear(n):
	a = [1]
	for i in range(0, n+10):
		a.append(2*a[i] + 1)
		a.append(3*a[i] + 1)
	a.sort()
	return a[n]
	
print(dbl_linear(100000))