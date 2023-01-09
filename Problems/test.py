class Solution:
    def productExceptSelf(self, nums):
        prefix = 1
        postfix = 1 
        res = []
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        print(res)
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
S = Solution()

print(S.productExceptSelf([1,2,3,4]))
#print(S.productExceptSelf([0,0,0,0]))
#print(S.productExceptSelf([4,3,2,1]))
#print(S.productExceptSelf([5,6,4,0]))