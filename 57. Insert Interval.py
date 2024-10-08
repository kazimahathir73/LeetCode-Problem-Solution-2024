class Solution:
  def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

    new_interval = []
    i = 0

    while i < len(intervals):
        if intervals[i][1] >= newInterval[0]:
            break
        new_interval.append(intervals[i])
        i += 1


    while i < len(intervals):
        if intervals[i][0] > newInterval[1]:
            break
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    new_interval.append(newInterval)

    while i < len(intervals):
        new_interval.append(intervals[i])
        i += 1

    return new_interval

obj = Solution()
print(obj.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(obj.insert([[1,3],[6,9]], [2,5]))