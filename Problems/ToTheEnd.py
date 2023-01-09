def dbl_linear(n):
    a = [1]
    b = [1]
    for i in range(n):
        x = min(a[0], b[0])
        a.append(2 * x + 1)
        b.append(3 * x + 1)
        if x in a:
            a.remove(x)
        if x in b:
            b.remove(x)
    return min(a[0], b[0])

def dbl_linear2(n):
    x = [1]
    for i in x:
        x.append((i * 2) + 1)
        x.append((i * 3) + 1)
        if len(x) > n *10:
            print(x)
            break
    return sorted(list(set(x)))[n]

print(dbl_linear2(10))