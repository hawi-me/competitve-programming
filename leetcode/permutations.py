class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            for n in nums:
                if n in path:
                    continue
                path.append(n)
                backtrack()
                path.pop()       
        ans=[]
        path=[]
        backtrack()
        return ans