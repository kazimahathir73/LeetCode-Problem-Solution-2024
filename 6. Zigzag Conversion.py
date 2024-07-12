class Solution():
    def convert(self, s, numRows):
        str1 = ''

        jump = (numRows-1)*2
        for i in range(numRows):
            for k in range(i,len(s),jump):
                str1 += s[k]
                if i > 0 and i < len(s)-1 and k+jump-2*i < len(s):
                    str1 += s[k+jump-2*i]
        return str1

obj = Solution()
print(obj.convert("PAYPALISHIRING",4))