def find_uniq(arr):
    arr.append(arr[2])
    for i in arr:
        if i[0].lower() not in arr[-1].lower():
            return i
    return arr[0]
#print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))
#print(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]))
#print(find_uniq([ "s", "ad", "da"]))
#print(find_uniq([ '    ', 'a', '  ' ]))

#print("f","o","b" in "foobs")