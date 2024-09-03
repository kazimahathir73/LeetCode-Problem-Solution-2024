class Solution:
    def getLucky(self, s, k):
        dict_a = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
                   'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 
                   'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 
                   'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 
                   'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
        
        str_f = ''
        for l in s:
            str_f += dict_a[l]
        
        for i in range(k):
            str_d = 0
            for l in str_f:
                str_d += int(l)
            str_f = str(str_d)  
        return int(str_f)

obj = Solution()
print(obj.getLucky("iiii", 1)) 
