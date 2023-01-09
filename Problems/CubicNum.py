def is_sum_of_cubes(s):
    summ = 0
    a = []
    b = False
    num = 0
    res = ""
    s += "-"
    for i in s:
        if num == 3:
            if len(a) == 3 and int(a[0])**3 + int(a[1])**3 + int(a[2])**3 == int(''.join(a)):
                res += "".join(a) + " "
                summ += int(''.join(a))
            elif len(a) == 2 and int(a[0])**3 + int(a[1])**3 == int(''.join(a)):
                res += "".join(a) + " "
                summ += int(''.join(a))
            elif a[0] == 0 or a[0] == 1:
                res += str(a[0]) + " " 
                summ += int(a[0])
            a.clear()
            b = False
            num = 0
        if i in "1234567890":
            a.append(i)
            num += 1
            b = True
        else:
            if b:

                if len(a) == 3 and int(a[0])**3 + int(a[1])**3 + int(a[2])**3 == int(''.join(a)):
                    res += "".join(a) + " "
                    summ += int(''.join(a))
                elif len(a) == 2 and int(a[0])**3 + int(a[1])**3 == int(''.join(a)):
                    res += "".join(a) + " "
                    summ += int(''.join(a))
                elif a[0] == "0" or a[0] == "1":
                    res += str(a[0]) + " " 
                    summ += int(a[0])
                a.clear()
                num = 0
                b = False
    if len(res) == 0:
        return "Unlucky"
    else:
        return res + str(summ) + " Lucky"
print(is_sum_of_cubes("&z _upon 407298a --- ???ry, ww/10 I thought, 631str*ng and w===y -721&()"))
print(is_sum_of_cubes("0 9026315 -827&()"))
print(is_sum_of_cubes("##' ullamco :# ,',, 1 voluptate exercitation 3711531530 !: 4074073711 id velit ? 1 371153371 153407371 ,# dolore aute ;, 153407 et !~ 407 laboris deserunt 0 :# ,~ 371"))


def is_sum_of_cubes2(s):
    summ = 0
    a = []
    b = False
    num = 0
    res = ""
    s += "-"
    for i in s:
        if num == 3:
            if int(''.join(a)) in [0,1,153,370,371,407]:
                res += "".join(a) + " "
                summ += int(''.join(a))
            a.clear()
            b = False
            num = 0
        if i in "1234567890":
            a.append(i)
            num += 1
            b = True
        else:
            if b:

                if int(''.join(a)) in [0,1,153,370,371,407]:
                    res += "".join(a) + " "
                    summ += int(''.join(a))
                a.clear()
                num = 0
                b = False
    if len(res) == 0:
        return "Unlucky"
    else:
        return res + str(summ) + " Lucky"
print(is_sum_of_cubes2("&z _upon 407298a --- ???ry, ww/10 I thought, 631str*ng and w===y -721&()"))
print(is_sum_of_cubes2("0 9026315 -827&()"))
print(is_sum_of_cubes2("##' ullamco :# ,',, 1 voluptate exercitation 3711531530 !: 4074073711 id velit ? 1 371153371 153407371 ,# dolore aute ;, 153407 et !~ 407 laboris deserunt 0 :# ,~ 371"))



