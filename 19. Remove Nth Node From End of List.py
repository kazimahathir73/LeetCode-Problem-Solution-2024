# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        
        current = head
        leng = 0
        while current != None:
            leng+=1
            current=current.next

        if leng < n:
            return head
        
        if leng-n == 0:
            if leng == 1 and n == 1:
                return None
            else:
                return head.next
        
        idx = 0
        current = head
        while current != None:
            if idx == leng-n-1:
                current.next = current.next.next
            idx+=1
            current = current.next

        return head
        