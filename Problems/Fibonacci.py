def nth_fib(n):
    f = [0,1]
    if n == 1:
        return 0
    else:
        for i in range (1,n-1):
            f.append(f[i-1] + f[i])
    return max(f)

def nth_fib2(n):
  a, b = (0, 1)
  for _ in range(n-1):
    a, b = b, a + b
  return a

def nth_fib3(n):
  if n==1:
      return 0
  elif n==2:
      return 1
  else:
      return nth_fib(n-1)+nth_fib(n-2)

print(nth_fib(11))
print(nth_fib2(10))
print(nth_fib2(7))