class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        total = 0
        def backtrack(start, path,total):
            if len(path) == k and total == n:
                ans.append(path[:])
                return
            for i in range(start,10):
                path.append(i)
                total += i
                backtrack(i + 1 ,path,total)
                p = path.pop()
                total -= p
        ans=[]
        backtrack(1,[],total)
        return ans