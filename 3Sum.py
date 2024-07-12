class Solution():
    def threeSum(self, nums):
        nums = sorted(nums)
        output = set()
        for k in range(len(nums)):
            target = -nums[k]
            i,j = k+1, len(nums)-1
            while i < j:
                sum_two = nums[i] + nums[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    output.add((nums[k],nums[i],nums[j]))
                    i += 1
                    j -= 1
        return output

obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))
            