from collections import Counter 


def topKFrequent(nums, k):
    nums = Counter(nums)
    return [x for x,_ in nums.most_common(k)]

print(topKFrequent([1,1,1,2,2,3], 2))
        
        