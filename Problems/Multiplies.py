def solution(number):
    res = 0
    if number <= 0:
        return 0
    else:
        a = [i for i in range(1,number)]
        for i in a:
            if i % 3 == 0 or i % 5 == 0:
                res += i
        return res
    #return sum(i for i in range (number) if i % 3 == 0 or i % 5 == 0)
print(solution(15))