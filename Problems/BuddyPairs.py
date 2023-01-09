def buddy(start, limit):
    summ = []
    count = 0
    res = []
    for i in range(start, limit):
        for j in range(1,i):
            if i % j == 0:
                summ.append(j)
        for g in range(1, sum(summ)):
            if sum(summ) % g == 0:
                count += g 
        if sum(summ) == count and i != count:
            return sum(summ), count
        else:
            count = 0
            summ.clear()
    return "Nothing"

print(buddy(10, 50))