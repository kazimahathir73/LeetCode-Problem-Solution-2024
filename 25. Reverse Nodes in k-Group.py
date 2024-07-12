class Solution():
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getkth(groupPrev, k)
            if not kth: 
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next =prev
                prev = curr
                curr = temp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next
    
    def getkth(self, curr, k):
            while curr and k:
                curr = curr.next
                k -= 1
            return curr



