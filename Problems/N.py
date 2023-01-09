
def green(n):
    f = "5"
    nums = [5, 6]
    s = "6"
    if n == 1:
        return 1
    for j in range(0, n//2):
        for i in range(1, n*20):
            i = int(str(i) + f)
            if str(i**2)[-len(str(i)):] == str(i):
                nums.append(i)
                f = str(i)
                break
    for j in range(0, n//2):
        for i in range(1, n*20):
            i = int(str(i) + s)
            if str(i**2)[-len(str(i)):] == str(i):
                nums.append(i)
                s = str(i)
                break
    nums.sort()
    return nums

def green2(n):
    if n==1:return n
    a,b,m,p=5,6,3,10
    while m<n:
        c=pow(a,2,p)
        d=p+1-c
        a,b,p,m=c,d,p*10,m+2-(a==c)-(b==d)
    return max(a,b) if m==n else min(a,b)

print(green(1000))