# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    flag = 0   
    def isSameTree(self, p, q):
        if p == None and q != None:
            self.flag = 1
            return
        elif q == None and p != None:
            self.flag = 1
            return
        elif p == None or q == None:
            return True
        
        if p.val != q.val:
            self.flag = 1
           
        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)

        if self.flag == 0:
            return True
        else:
            return False