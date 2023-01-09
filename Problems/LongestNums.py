def longestConsecutive(nums: list[int]) -> int:
    nums = sorted(list(set(nums)))
    prev = nums[0]
    nums.append(0)
    max = 0
    count = 1
    print(nums)
    for i in range(1, len(nums)):
        print(prev, nums[i])
        if nums[i] - 1 == prev:
            count += 1
            prev = nums[i]
            print("fede")
        else:
            if count > max:
                max = count
                count = 1
            if count >= len(nums) - count:
                return count
            prev = nums[i]
    if count == len(nums):
        return count
    return max

print(longestConsecutive([-8,-4,9,9,4,6,1,-4,-1,6,8]))