# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root):
        
        if root == None:
            return []
        
        arr_l = []
        queue = deque([root])

        while len(queue) != 0:
            arr = []
            length = len(queue)
            for i in range(length):
                pop_n = queue.popleft()
                arr.append(pop_n.val)

                if pop_n.left != None:
                    queue.append(pop_n.left)
                if pop_n.right != None:
                    queue.append(pop_n.right)
            
            arr_l.append(arr)
        
        return arr_l
