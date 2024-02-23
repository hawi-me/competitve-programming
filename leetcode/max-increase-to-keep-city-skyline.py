class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col={}
        dictt={}
        diff =0 
        for i in range(len(grid)):
            dictt[i] = max(grid[i])
        for j in range(len(grid[0])):
            cols=[]
            for i in range(len(grid)):
                cols.append(grid[i][j])
            col[j] = max(cols)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff += min(dictt[i],col[j]) - grid[i][j]
        return diff
    
            
        