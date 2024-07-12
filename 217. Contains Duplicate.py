class Solution():
    def containsDuplicate(self, nums):
        arr = sorted(nums)

        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                return True
        return False

obj1 = Solution()
print(obj1.containsDuplicate([1,2,3,4]))