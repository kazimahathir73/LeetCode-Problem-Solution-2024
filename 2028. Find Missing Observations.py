class Solution:
    def missingRolls(self, rolls, mean, n):

        rem = (mean*(len(rolls)+n)) - sum(rolls)
        avg_r = (rem)//n

        if rem > (n*6) or n > rem:
            return []
        
        arr = []
        for i in range(n):
            arr.append(avg_r)
            rem -= avg_r

        if rem == 0:
            return arr
        
        for i in range(n):
            arr[i]+=1
            rem-=1
            if rem <= 0:
                break

        return arr

        