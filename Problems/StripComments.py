def strip_comments(strng, markers):
    strng = strng.split(markers[0])
    s1 = strng[0]
    s2 = strng[1]
    x1 = strng[1].find("/n")
    x2 = strng[1].find(markers[1])
    res = s1[:-1] + s2[x1 : x2 + 1]
    return res

print(strip_comments('apples, pears # and bananas/ngrapes/nbananas !apples', ['#', '!']))