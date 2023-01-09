def ascii_encrypt(plaintext):
    res = ''
    for count, i in enumerate(plaintext):   
        res += chr(ord(i) + count)
    return res
    #return ''.join(chr(ord(i) + c) for c, i in enumerate(plaintext))
    
def ascii_decrypt(plaintext):
    res = ''
    for count, i in enumerate(plaintext):   
        res += chr(ord(i) - count)
    return res
    #return ''.join(chr(ord(i) - c) for c, i in enumerate(plaintext))


print(ascii_encrypt('password'))
print(ascii_decrypt('pbuv{txk'))