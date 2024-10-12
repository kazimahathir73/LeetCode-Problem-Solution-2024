class Solution:
    def merge(self, intervals):
        intervals.sort()
        new_interval = [intervals[0]]
        i = 1
        while i <= len(intervals)-1:
            if ( new_interval[-1][0] <= intervals[i][0] <= new_interval[-1][1]) or (new_interval[-1][0] <= intervals[i][1] <= new_interval[-1][1]):
                start, end = min(intervals[i][0], new_interval[-1][0]), max(intervals[i][1], new_interval[-1][1])
                new_interval.pop()
                new_interval.append([start,end])
            else:
                new_interval.append(intervals[i])
            i+=1

        return new_interval

obj = Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))