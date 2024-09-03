class Solution:
    def chalkReplacer(self, chalk, k):
        
        rem = k-(sum(chalk)*int(k/sum(chalk)))
        if rem < 0:
            return 0
        for i in range(len(chalk)):
            rem-=chalk[i]
            if rem < 0:
                return i
                
obj = Solution()
print(obj.chalkReplacer([3,4,1,2], 25))   