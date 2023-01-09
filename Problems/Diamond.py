def diamond(n):
    if n <=0 or n % 2 == 0:
        return None
    else:
        res = ""
        num = n // 2
        for i in range(1, n, 2):
            res += " "*num
            res += ("*"*i) + "\n"
            num -= 1
        num == 0
        for i in range(n, 0, -2):
            res += " "*num
            res += ("*"*i) + "\n"
            num += 1
    return(res)
print(diamond(101))