class Solution:
    def construct2DArray(self, original, m, n):

        if len(original) != m*n:
            return []
        
        arr= []
        idx = 0
        for i in range(m):
            arr_r = []
            for j in range(n):
                arr_r.append(original[idx])
                idx+=1
            arr.append(arr_r)

        return arr

obj = Solution()
print(obj.construct2DArray([1,2,3,4], 2, 2))
        