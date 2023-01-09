# Recursing Programming
def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)

# Dynamic Programming
def fib2(n):
	f = [0] * (n*10)
	f[0] = 0
	f[1] = 1
	for i in range(2, n+1):
		f[i] = f[i-1] + f[i-2]
	return f[n]

#print(fib(30))
print(fib2(100000))