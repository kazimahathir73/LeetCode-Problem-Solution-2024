class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ''
        if s == t:
            return s
        
        dict_s = {}
        dict_d = {}

        ans = float("inf"), None, None
        
        for itm in t:
            if itm not in dict_s:
                dict_s[itm] = 1
                dict_d[itm] = 0
            else:
                dict_s[itm] += 1
        
        l = 0
        r = 0
        have = 0
        need = len(t)
        while l != len(s):
            if s[l] in dict_d:
                dict_d[s[l]] += 1
                if dict_d[s[l]] <= dict_s[s[l]]:
                    have+=1

            if have == need:
                


obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))
