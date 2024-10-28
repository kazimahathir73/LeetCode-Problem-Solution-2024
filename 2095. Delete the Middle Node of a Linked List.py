# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        current = head
        leng = 0
        while current != None:
            leng+=1
            current=current.next

        if leng == 1:
            return None
        
        if leng == 2:
            head.next = None
            return head
        
        current = head
        idx = 0
        while current != None:
            if idx == (leng//2)-1:
                current.next = current.next.next
            idx+=1
            current = current.next
        
        return head