import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8],
			[9,10,11,12], [13,14,15,16]])
m = np.reshape(a, (4, 4))
print(m)
print("----------------")

m = np.append(m,[[-3,-2,-1,0]], 0)
print(m)
print("----------------")

m = np.delete(m, [1], 0)
print(m)