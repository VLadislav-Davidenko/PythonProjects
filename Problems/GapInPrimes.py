def gap(g, m, n):
    a = []
    b = [2]
    res = []
    ans = ''
    x = 0
    for i in range(m, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            a.append(i)
    a.append(0)
    for i in range(len(a)-1):
        if a[i+1]  - a[i] == g:
            res.append(a[i])
        elif len(res) != 0:
            res.append(a[i])
            if len(ans) < len(res):
                ans = ' '.join(str(a) for a in res)
                res.clear() 
    if len(ans) == 0:
        return None
    return [int(i) for i in ans.split()]


print(gap(2, 100, 110))
print(gap(6,100,110))
print(gap(2,100,103))
print(gap(10, 300, 400))