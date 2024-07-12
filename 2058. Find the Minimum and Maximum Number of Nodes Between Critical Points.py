# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        arr = []
        idx = 2
        c_n = head.next
        prev_val = head.val
        while c_n.next != None:
            if (c_n.val < prev_val and c_n.val < c_n.next.val) or (c_n.val > prev_val and c_n.val > c_n.next.val):
                arr.append(idx)
            prev_val = c_n.val
            c_n = c_n.next
            idx+=1
        
        arr_l = []
        if len(arr) <= 1:
            arr_l.append(-1)
            arr_l.append(-1)
        elif len(arr) == 2:
            arr_l.append(arr[1]-arr[0])
            arr_l.append(arr[1]-arr[0])
        elif len(arr) >= 2:
            min_l = float('inf')
            for i in range(len(arr)-1):
                if arr[i+1] - arr[i] < min_l:
                    min_l = arr[i+1] - arr[i]
            arr_l.append(min_l)
            arr_l.append(arr[-1]-arr[0])
        
        return arr_l
        
