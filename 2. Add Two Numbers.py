
class ListNode():
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
       
class Solution():
    def addTwoNumbers(self, l1, l2):
        
        str1 = ''
        cn1 = l1
        while cn1 != None:
            str1 += str(cn1.val)
            cn1 = cn1.next

        str2 = ''
        cn2 = l2
        while cn2 != None:
            str2 += str(cn2.val)
            cn2 = cn2.next

        str3 = ''
        str4 = ''
        for j in range(len(str1)-1,-1,-1):
            str3 += str1[j]
        
        for k in range(len(str2)-1,-1,-1):
            str4 += str2[k]

        result = str(int(str3)+int(str4))

        h1 = ListNode(result[-1])
        cn3 = h1
        for i in range(len(result)-2,-1,-1):
            obj1 = ListNode(result[i])
            cn3.next = obj1
            cn3 = cn3.next
        
        return h1
    


        
        
        

ob1 = Solution()
ob1.addTwoNumbers([2,4,3], [5,6,4])
