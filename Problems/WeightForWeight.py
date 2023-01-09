def order_weight(strng):
	a = strng.split()
	res = []
	for i in a:
		summ = sum([int(j) for j in i])
		res.append(summ)
	return " ".join([x for _,x in sorted(zip(res, a))])

def weight_key(s):
	a = (sum(int(c) for c in s), s)
	return (sum(int(c) for c in s), s)
def order_weight2(s):
    return ' '.join(sorted(s.split(' '), key=weight_key))

print(order_weight("103 123 4444 99 2000"))
print(order_weight2("103 123 4444 99 2000"))

