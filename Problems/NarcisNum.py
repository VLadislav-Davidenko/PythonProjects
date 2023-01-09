def is_narcissistic(i):
	a = list(str(i))
	n = len(a)
	res = 0
	for j in a:
		res += (int(j)**n)
	return i == res
print(is_narcissistic(1634))