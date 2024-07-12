class Solution():
    def productExceptSelf(self, nums):
        left = [1]*len(nums)
        right = [1]*len(nums)

        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]

        for j in range(len(nums)-2,-1,-1):
            right[j] = nums[j+1] * right[j+1]

        for k in range(len(left)):
            left[k] = left[k]*right[k]

        return left
    
obj1 = Solution()
print(obj1.productExceptSelf([1,2,3,4]))