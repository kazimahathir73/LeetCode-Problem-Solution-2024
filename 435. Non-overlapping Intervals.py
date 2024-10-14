class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda t: t[1])
        count = 0
        end = float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                count+=1 
        
        return count

obj = Solution()
print(obj.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))