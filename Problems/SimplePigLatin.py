def pig_it(text):
    a = text.split()
    res = ''
    for i in a:
        if i not in ',.?!:;"':
            res += i[1:] + i[:1] + "ay"
        else:
            res += i
        res += " "
    #return res.strip()
    return " ".join(word[1:] + word[:1] + "ay" if word.isalpha() else world for word in a)
print(pig_it("Pig latin is cool"))