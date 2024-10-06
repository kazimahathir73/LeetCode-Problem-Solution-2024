# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head, k):

        c_n = head
        count = 0
        while c_n != None:
            count+=1
            c_n=c_n.next
        
        f_arr = []
        for p in range(k):
            f_arr.append([])

        div = count//k
        rem = count%k
        c_n1 = head
        prev = None
        for i in range(k):
            if i >= count:
                break

            if rem > 0:
                itr = div + 1
                rem-=1
            else:
                itr = div

            c_n2 = c_n1
            for j in range(itr):
                if j == 0:
                    f_arr[i] = c_n2
                else:
                    prev = c_n2
                    c_n2 = c_n2.next
            prev.next = None
            c_n1 = c_n2

        return f_arr

n1 = ListNode(1)
n2 = ListNode(2,n1)
n3 = ListNode(3,n2)
obj = Solution()
print(obj.splitListToParts(n1,5))