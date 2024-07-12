class Solution():
    def maxSubArray(self, nums):
        max_val = float('-inf')
        
        for i in range(len(nums)):
            total = 0
            for j in range(i,len(nums)):
                total += nums[j]
                if total > max_val:
                    max_val = total
        
        return max_val

obj1 = Solution()
print(obj1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))