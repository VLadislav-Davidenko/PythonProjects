def closest(s):
    dif = 1000
    s = s.split()
    num1 = []
    num2 = []
    if len(s) == 0:
        return []
    for i in s:
        x = 0
        for g in i:
            x += int(g)
        y = s.index(i)
        z = int(i)
        for j in s:
            x1 = 0
            for h in j:
                x1 += int(h)
            y1 = s.index(j)
            z1 = int(j)
            if i != j and x1 - x <= dif and x1 - x >= 0:
                dif = x1 - x
                num1.clear()
                num2.clear()
                num1 = [x, y, z]
                num2 = [x1, y1, z1]
                x,x1,y,y1,z,z1 = 0,0,0,0,0,0
    return [num1, num2]

print(closest("103 123 4444 99 2000"))
#print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"))

