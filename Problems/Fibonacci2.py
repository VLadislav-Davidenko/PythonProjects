def fib_digits(n):
    f = [0,1]
    res1 = []
    res2 = []
    ans = []
    count = 0
    if n == 1:
        return 0
    else:
        n += 1
        for i in range (1,n-1):
            f.append(f[i-1] + f[i])
    print(f)
    for i in range(1,10):
        for j in f:
            if str(i) in str(j):
                count += 1
                
        if count != 0:
            res1.append(i)
            res2.append(count)
            count = 0
    res2, res1 = zip(*[(b, a) for b, a in sorted(zip(res2, res1))])
    for i in range(len(res2)-1, 0, -1):
        a = (res2[i], res1[i])
        ans.append(a)
    return ans

print(fib_digits(10))