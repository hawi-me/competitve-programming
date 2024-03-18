# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lis=[] 
        def inorder(root , lis):
            if not root:
                return 
            inorder(root.left,lis)
            lis.append(root.val)
            inorder(root.right,lis)
        def balance_bst(lis,l,r):
            if l > r:
                return None
            mid = (l+r)//2
            node = TreeNode(lis[mid])
            node.left = balance_bst(lis,l,mid-1)
            node.right = balance_bst(lis,mid+1,r)
            return node
        inorder(root,lis)
        return balance_bst(lis,0,len(lis)-1)
        