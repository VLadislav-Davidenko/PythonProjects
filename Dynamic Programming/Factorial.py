# Tabulated version to find factorial x
def factorial(n):
	dp = [0] * (n  * 10)
	dp[0] = 1
	for i in range(1, n+1):
		dp[i] = dp[i-1] * i
	return dp[n]

# Memoized version to find factorial x.
#  To speed up we store the values
# of calculated states

# initialized to -1
def factorial2(x):
	dp[0] * (n * 10)
	
	# return fact x!
	def solve(x):
	   if (x == 0):
	       return 1
	   if (dp[x]!=-1):
	       return dp[x]
	   return (dp[x] == x * solve(x-1))

print(factorial(10000))