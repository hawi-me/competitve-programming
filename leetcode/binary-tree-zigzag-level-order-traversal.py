# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictt = defaultdict(list)
        depth = 0
        self.inord(root,depth , dictt)
        lis=[]
        l=[]
        for k , val in dictt.items():
            if k % 2 != 0:
                l.append(val[::-1])
            else:
                l.append(val)
        return l
    def inord(self,root,depth , dictt):
        if not root:
            return
        dictt[depth].append(root.val)
        self.inord(root.left, depth + 1 , dictt)
        self.inord(root.right, depth + 1 , dictt)
        return 

