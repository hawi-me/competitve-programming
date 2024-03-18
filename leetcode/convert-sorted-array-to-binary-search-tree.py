# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def balance_bst(nums,l,r):
            if l > r:
                return None
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = balance_bst(nums,l,mid-1)
            node.right = balance_bst(nums,mid+1,r)
            return node
        return balance_bst(nums,0,len(nums)-1)
        