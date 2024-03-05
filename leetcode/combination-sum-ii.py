class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        total=0
        ans=[]
        candidates.sort()
        prev = 0
        def backtrack(i ,path,total):
            if total == target :
                ans.append(path[:])
                return
            if total  > target:
                return
            for j  in range(i,len(candidates)): 
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                path.append(candidates[j])
                total+=candidates[j]
                backtrack(j + 1, path, total)
                prev = path.pop()
                total-= prev
        backtrack(0,[],total)
        return ans
