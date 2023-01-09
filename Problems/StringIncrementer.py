def increment_string(strng):
    x = 0
    strng = "AB" + strng
    for i in range(len(strng)-1, 0, -1):
        if strng[i] in "0123456789":
            x += 1
        elif strng[i] not in "0123456789" and x != 0:
            count =  len(strng[-x:])
            num = int(strng[-x:]) + 1
            if len(str(num)) > count:
                count = len(str(num))
            return strng[2:i+1] + ("{:0100d}".format(num))[-count:]
    return strng[2:] + "1"

def increment_string2(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    print("Dad".zfill(10))
    return head + str(int(tail) + 1).zfill(len(tail))

print(increment_string2("foo"))
print(increment_string2("Sr099"))
print(increment_string2("TTT009"))
print(increment_string2("SS99"))
print(increment_string2("99"))