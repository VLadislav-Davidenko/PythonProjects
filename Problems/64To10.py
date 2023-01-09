b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
a = list(b64)
def base64_to_base10(n):
  summ = 1
  if len(n) == 1:
    return a.index(n)
  else:
    res = 64 ** (len(n)- 1)
    res *= a.index(n[0]) 
    for i in range(1,len(n)-1):
      res += (a.index(n[i]) * 64)
    res += (a.index(n[-1]))
    return res
def base64_to_base10_2(str):
    res = 0
    for c in str:
        res *= 64
        res += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".find(c)
    return res
print(base64_to_base10("Python")) 
print(base64_to_base10_2("Python")) 