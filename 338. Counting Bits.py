class Solution:
    def countBits(self, n: int):
        arr = []
        for i in range(n+1):
            arr.append(bin(i).count("1"))
        
        return arr

