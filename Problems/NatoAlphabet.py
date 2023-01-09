nato = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]
def to_nato(words):
    res = ''
    str = words.split()
    str = ''.join(str).upper()
    for i in str:
        for j in nato:
            if i in j:
                res += j + " "
        if i in ",.!?":
            res += i + " "
    return res.strip()
print(to_nato("I Love You !"))