def min_permutation(n):
    x = []
    res = ''
    if n >= 0:
        zeroes = 0
        for i in str(n):
            if i == '0':
                zeroes += 1
            x.append(int(i))
        x.sort()
        for j in range(len(x)):
            res += str(x[j])
        res = str(int(res))
        res = res[:1] + '0'*zeroes + res[1:]
        return int(res)
    else:
        zeroes = 0
        n *= -1
        for i in str(n):
            if i == '0':
                zeroes += 1
            x.append(int(i))
        x.sort()
        print(x)
        for j in range(len(x)):
            res += str(x[j])
        res = str(int(res))
        res = res[:1] + '0'*zeroes + res[1:]
        return int(res) * -1

def min_permutation2(n):
    b = n < 0
    s = ''.join(sorted(str(abs(n))))
    n = s.count("0")
    s = s.replace("0", "")
    return int(s[:1] + "0"*n + s[1:] * (-1 if b else 1))
print(min_permutation(10))
print(min_permutation2(-6738234))