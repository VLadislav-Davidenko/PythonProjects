from math import prod
def productExceptSelf(nums):
    n = None
    if 0 in nums:
        n = nums.index(0)
        nums.pop(n)
        res = [0] * len(nums)
    else:
        res = [prod(nums)] * len(nums)
    if len(num)

    for x, i in enumerate(nums):
        if n == x:
            res.insert(x, 0)
            res[x] = prod(nums)
        else:
            res[x] = int(res[x]/i)
    return res


print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
print(productExceptSelf([1,0]))