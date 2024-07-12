class Solution():
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        
        l = min(bloomDay)
        h = max(bloomDay)
        
        while l < h:
            mid = (h + l) // 2
            flower = 0
            bon = 0
            var = False
            print(mid)

            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    flower += 1
                    if flower == k:
                        bon += 1
                        flower = 0
                        if bon >= m:
                            var = True
                            break
                else:
                    flower = 0
            
            if var:
                h = mid
            else:
                l = mid+1
        
        return l

obj = Solution()
print(obj.minDays([1,10,3,10,2], 3, 1)) 
print(obj.minDays([1,10,3,10,2], 3, 2)) 
print(obj.minDays([7,7,7,7,12,7,7], 2, 3))
