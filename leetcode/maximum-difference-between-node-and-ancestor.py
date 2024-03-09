# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # ans = 0   

        # def inor(root, maxx, minn):
        #     if not root:
        #         return maxx, minn
            
        #     nonlocal ans 
        #     if not root.right and not root.left:
        #         curr_max = root.val
        #         curr_min = root.val
        #     elif not root.right:
        #         curr_max = max(root.val, inor(root.left, maxx, minn)[1])
        #         curr_min = min(inor(root.left, maxx, minn)[0], root.val)
        #     elif not root.left:
        #         curr_max = max(root.val, inor(root.right, maxx, minn)[1])
        #         curr_min = min(inor(root.right, maxx, minn)[0], root.val)
        #     else:
        #         left_min, left_max = inor(root.left, maxx, minn)
        #         right_min, right_max = inor(root.right, maxx, minn)
        #         curr_max = max(left_max, right_max)
        #         curr_min = min(left_min, right_min)
            
        #     ans = max(ans, abs(root.val - curr_max), abs(root.val - curr_min))
            
        #     return min(root.val, curr_min), max(root.val, curr_max)
        
        # inor(root, float('-inf'), float('inf'))
        # return ans
        max_diff = 0
        def calculate(node,min_val,max_val):
            nonlocal max_diff
            if not node:
                return 
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            max_diff = max(max_diff,abs(min_val-max_val))
            calculate(node.right,min_val,max_val)
            calculate(node.left,min_val,max_val)
        calculate(root,root.val,root.val)
        return max_diff




