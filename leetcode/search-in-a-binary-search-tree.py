# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root :
            return None 
        return self.search(root , val) 
    def search(self,root ,num ):
        if not root :
            return None 
        if num > root.val:
            return self.search(root.right,num)
            
        if num < root.val:
            return self.search(root.left,num)
            
        if num == root.val:
            cur=TreeNode(root.val)
            cur.left = root.left
            cur.right = root.right
            return cur
            
        