def solve(eq: str):
    summ = 0
    ar = 1
    res = []
    revers = False
    a = eq.split(" ")
    for i in range(len(a)):
        if a[i] == 'x':
            ar = 1
        elif a[i] == '+':
            ar = 1
        elif a[i] == '-':
            if a[i + 1] == 'x':
                revers = True
            ar = -1
        elif a[i] == "=":
            res.append(summ)
            summ = 0
            ar = 1
        else:
            summ += int(a[i])*ar
    res.append(summ)
    if a.index("x") < a.index("="):
        if revers:
            return int(res[0]) - int(res[1])
        else:
            return int(res[1]) - int(res[0])
    else:
        if revers:
            return int(res[1]) - int(res[0])
        else:
            return int(res[0]) - int(res[1]) 

def solve2(eq_str):
    (lft, rgt) = eq_str.split('=')
    if 'x' in rgt:
        lft, rgt = rgt, lft
    if '- x' in lft:
        lft, rgt = rgt, lft
    x = 0
    return eval(rgt) - eval(lft)
print(solve("- x - 1 = 8"))
print(solve("- 9358 + 3569 - x = 946047"))
print(solve("- x = - 1"))
print(solve("x = 9"))