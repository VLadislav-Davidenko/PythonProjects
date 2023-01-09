def last_man_standing(n):
	values = [i for i in range(1, n+1)]
	while len(values) != 1:
		del values[0::2]
		values = values[::-1]
		#values = values[1::2][::-1]
	return max(values)
print(last_man_standing(9))