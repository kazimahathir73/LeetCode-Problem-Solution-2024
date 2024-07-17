# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):

        if root == None:
            return 0
        
        m1 = self.maxDepth(root.left)
        m2 = self.maxDepth(root.right)

        return max(m1, m2) + 1



        