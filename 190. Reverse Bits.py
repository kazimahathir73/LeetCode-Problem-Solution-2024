class Solution:
    def reverseBits(self, n):
        bit = 00000000000000000000000000000000
        
        for i in range(32):
            if (n >> (32-i-1)) & 1 == 1:
                bit = bit | (1 << i)
            else:
                bit = bit | (0 << i)
        
        return bit