def moving_shift(s, shift):
    res = ''
    for count, i in enumerate(s):   
        res += chr(ord(i) + shift)
    n = len(res.split(chr(ord(" ") + shift)))
    
    return res

def demoving_shift(s, shift):
    res = ''
    for count, i in enumerate(s):   
        res += chr(ord(i) - shift)
    return res

print(moving_shift("I should have known that you would have a perfect answer for me!!!", 1))