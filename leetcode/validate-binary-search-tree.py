# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lis=[]
        self.inor(root , lis)
        lis2 = sorted(lis)
        if len(lis) != len(set(lis)):
            return False
        if lis == lis2:
            return True
        else:
            return False

    def inor(self, root , lis):
        if not root:
            return
        self.inor(root.left ,lis)
        lis.append(root.val)
        self.inor(root.right , lis)
        return True
        