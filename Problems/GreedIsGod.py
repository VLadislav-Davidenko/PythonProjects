from collections import Counter

def score(dice):
	c = Counter(dice)
	res = 0
	if c[1] == 2: res += 200
	if c[1] == 3: res += 1000
	if c[1] == 4: res += 1100
	if c[1] == 5: res += 1200
	if c[1] == 1: res += 100
	if c[6] == 3: res += 600
	if c[5] == 5: res += 600
	if c[5] == 3: res += 500
	if c[5] == 2: res += 100
	if c[5] == 4: res += 550
	if c[4] == 3: res += 400
	if c[3] == 3: res += 300
	if c[2] == 3: res += 200
	if c[5] == 1: res += 50
	return res
print(score([2, 3, 4, 6, 2]))
print(score([4, 4, 4, 3, 3]))
print(score([1, 1, 1, 3, 1]))
print(score([3, 3, 3, 3, 3]))