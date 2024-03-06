# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val01
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.findroot(root,0)
    def findroot(self, root ,s):
        if not root: 
            return 0
        s = s*10 + root.val
        if not root.right and not root.left:
            return s 
        return self.findroot(root.left,s)  + self.findroot(root.right,s)
