class Solution:
    def maxArea(self, height):
        r = 0
        l = len(height)-1

        max_a = 0
        while(r != l):
            max_a = max(max_a, ((l-r)*min(height[l],height[r])))
            if height[l] < height[r]:
                l-=1
            else:
                r+=1

        return max_a

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))