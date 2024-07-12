class Solution():
    def lengthOfLongestSubstring(self, s):
        
        idx = 0
        r = 0
        dic = {}
        min_num = 0
        while idx < len(s):
            if s[idx] not in dic:
                dic[s[idx]] = idx
                r+=1
            else:
                r = 1
                dic = {s[idx]:idx}

            if r > min_num:
                min_num = r
  
            idx+=1
        if len(s) == 1:
            return 1
        else:
            return min_num

obj1 = Solution()
obj1.lengthOfLongestSubstring("abcabcbb")