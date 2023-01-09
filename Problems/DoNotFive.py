def dont_give_me_five(start, end):
    a = (end - start) // 10
    b = 9 ** ((end) // 50)
    print(a, b)
    return (end - start) - (b - a)

print(dont_give_me_five(-17, 9))
print(dont_give_me_five(1, 9))
#print(dont_give_me_five(984, 4304))
print(dont_give_me_five(50, 60))
#print(dont_give_me_five(40076, 2151514229639903569))