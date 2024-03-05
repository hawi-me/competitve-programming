class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i ,path):
            if tuple(path[:]) not in dictt:
                dictt[tuple(path[:])] = 1
                ans.add(tuple(sorted(path[:])))
            if i >= len(nums):
                return
            path.append(nums[i])
            backtrack(i + 1,path)
            path.pop()
            backtrack(i + 1,path)
        path=[]
        ans=set()
        l=0
        dictt = defaultdict()
        backtrack(0,path)
        return ans
            