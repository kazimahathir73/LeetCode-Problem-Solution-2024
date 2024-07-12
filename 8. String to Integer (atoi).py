class Solution():
    def myAtoi(self, s):
        str1 = ''
        num_checker = False

        for i in range(len(s)):
            if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                str1 += s[i]
                num_checker = True
            elif ord(s[i]) == 43 or ord(s[i]) == 45:
                if num_checker == True:
                    break
                str1 += s[i]

            elif (ord(s[i]) >= 33 and ord(s[i]) <= 47) or (ord(s[i]) >= 58 and ord(s[i]) <= 126):
                break
        
        if str1 == '':
            return 0
        
        str1 = int(str1)
        if str1 > 2**31-1:
            return 2**31-1
        elif str1 < -(2**31):
            return -(2**31)
        else:
            return str1

obj = Solution()
print(obj.myAtoi('words and 987'))
                