class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {"(":")", "{":"}", "[":"]"}
        s = list(s)
        a = 0
        
        for i in s:
            print(s)
            print(i)
            if i in dictionary:
                if dictionary.get(i) in s and s.index(i) + 1 == s.index(dictionary.get(i)):
                    a += 2
        return len(s) == a
s = Solution()
print(s.isValid("([)]"))

