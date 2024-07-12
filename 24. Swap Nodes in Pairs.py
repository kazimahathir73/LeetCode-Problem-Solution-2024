class Solution():
    def swapPairs(self, head):
        
        if head == None or head.next == None:
            return head
        
        count = 0
        c_n = head
        while c_n.next != None:
            if count%2 == 0:
                var = c_n.val
                c_n.val = c_n.next.val
                c_n.next.val = var            
            c_n = c_n.next
            count+=1
        return head
