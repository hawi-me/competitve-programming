# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lis = []
        self.inord(root,lis) 
        return lis[k - 1]

    def inord(self, root, lis):
        if not root:
            return
        self.inord(root.left , lis)
        lis.append(root.val)
        self.inord(root.right , lis)

        