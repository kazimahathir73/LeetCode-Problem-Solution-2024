class Solution():
    def missingNumber(self, nums):
        n = len(nums)
        nums = sorted(nums)
        for i in range(n):
            if i != nums[i]:
                return i
        return n

        