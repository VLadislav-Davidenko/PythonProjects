import ipaddress

def is_valid_IP(string):
    ans = False
    if string.count('.') == 3:
        a = string.split(".")
        for i in a:
            if i.isdigit() and int(i) >=0 and int(i) <= 255 :
                ans = True
            else:
                ans = False 
                break
    return ans
    #return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))

def is_valid_IP2(string):
    try:
        ipaddress.ip_address(strng)
        return True
    except:
        return False;



print(is_valid_IP("12.34.c.1")) 
print(is_valid_IP2("12.34.c.1")) 