# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=[]
        lis=[]
        self.move(root,dic)
        c=Counter(dic)
        maxi=0
        for k , v in c.items():
            lis.append(v)
        maxi=max(lis)
        res=[]
        for k , v in c.items():
            if c[k] == maxi:
                res.append(k)

        return res
    def move(self, root , dic):
        if not root:
            return 
        self.move(root.right,dic)
        self.move(root.left,dic)
        dic.append(root.val)
        


            
        
