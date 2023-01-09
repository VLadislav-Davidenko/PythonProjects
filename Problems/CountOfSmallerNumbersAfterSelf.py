from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, sorted_nums = [], sorted(nums)
        for i in nums:
            #ind = self.binary_search(sorted_nums, i)
            ind = bisect_left(sorted_nums, i)
            res.append(ind)
            del sorted_nums[ind]
        return res
    # Binery search that choose top left value
    def binary_search_left(self, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = (start+end)//2
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid 
        return start
    # Binery search that choose top right value
    def binary_search_right(self, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = (start+end)//2
            
            if nums[mid] > target:
                end = mid 
            else:
                start = mid + 1
        return start