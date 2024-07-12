class Solution():
    def maxProfit(self, prices):

        c_p = prices[0]
        r = 0
        for i in range(len(prices)):
            if prices[i] < c_p:
                c_p = prices[i]
            else:
                val = prices[i] - c_p
                r = max(val, r)

        return r

    
obj1 = Solution()
print(obj1.maxProfit([7,1,5,3,6,4]))
