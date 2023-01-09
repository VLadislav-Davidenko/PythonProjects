from collections import Counter
def top_3_words(text):
    text = text.replace("'", "")
    text = text.replace(" ", "")
    text.lower()
    res = Counter(text)
    ans = res.most_common(3)
    print(res)
    return [i[0] for i in ans]

print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))