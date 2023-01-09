class Solution(object):
	def groupAnagrams(strs):
		if len(strs) == 1 and strs[0] == "":
			return [[""]]
		f = []
		res = ["".join(sorted(list(i)))for i in strs]
		s = [x for _,x in sorted(zip(res, strs))]
		for x, i in enumerate(s):
			test = []
			for j in s:
				d = sum([ord(i) for i in i])
				if d == sum([ord(j) for j in j]) and i[0] in j:
					#print(j)
					test.append(j)
			if test not in f:
				f.append(test)
		return sorted(f, key=len)

print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))	