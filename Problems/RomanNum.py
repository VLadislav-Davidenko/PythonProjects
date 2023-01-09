ROMANS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}
    
class RomanNumerals:
    
    def to_roman(n):
        s = ''
        for key, value in ROMANS.items():
            while n % value != n:
                n = n - value
                s += key
        return s
    
    def from_roman(r):
        s = 0
        for key, value in ROMANS.items():
            while r.startswith(key):
                r = r[len(key):]
                s += value
        return s


print(RomanNumerals.to_roman(4000))
print(RomanNumerals.from_roman("MCMXLIX"))