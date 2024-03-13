# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def inorder(node,lis):
            if not node:
                return
            inorder(node.left,lis)
            lis.append(node.val) 
            inorder(node.right,lis)
        lis=[]
        inorder(root,lis)
        
        i=lis.index(low)
        j=lis.index(high)

        return sum(lis[i:j+1])
        