class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total=0
        ans=[]
        def backtrack(i ,path,total):
            if total == target:
                ans.append(path[:])
                return
            if total  > target:
                return
            for j  in range(i,len(candidates)): 
                path.append(candidates[j])
                total+=candidates[j]
                backtrack(j, path, total)
                total -= path.pop()
        backtrack(0,[],total)
        return ans
