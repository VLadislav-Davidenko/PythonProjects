from math import sqrt
def green(n):
    count = 0
    for i in range(1, n):
        if str(i**2)[-len(str(i)):] == str(i):
            count += 1
            print(count, i, i**2)
    return None
#print(green(1000000))
def count(n):
    f = "5"
    nums = [5, 6]
    s = "6"
    if n == 1:
        return 1
    for j in range(n):
        for i in range(1, n*10):
            i = int(str(i) + f)
            if str(i*i)[-len(str(i)):] == str(i):
                nums.append(i)
                f = str(i)
                break
    for j in range(n):
        for i in range(1, n*10):
            i = int(str(i) + s)
            if str(i*i)[-len(str(i)):] == str(i):
                nums.append(i)
                s = str(i)
                break
    nums.sort()
    return nums[n-2]
print(count(420))
print(count(12))