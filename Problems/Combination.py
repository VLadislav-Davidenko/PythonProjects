from math import factorial
def multiply(n, k):
    div = 2 
    ans = [1]
    while div <= n:
        if n % div == 0:
            ans.append(div)
            n = n / div
        else:
            div += 1
    x = factorial(len(ans))
    y = factorial(k)
    z = factorial(len(ans)-k)
    print(x/(y*z))
    print(x,y,z)
    return ans

print(multiply(24,2))