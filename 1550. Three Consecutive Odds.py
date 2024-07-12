class Solution:
    def threeConsecutiveOdds(self, arr):
        flag = False
        for i in range(len(arr)):
            if i <= len(arr)-3:
                if arr[i] % 2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0:
                    flag = True
                    break
                    
        return flag
                    
obj = Solution()
print(obj.threeConsecutiveOdds([2,6]))