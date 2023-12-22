class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def sums(row,col):
            ans=0
            for i in range(row,row+3):
                for j in range(col,col+3):
                    ans+=grid[i][j]
            ans-=grid[row+1][col]
            ans-=grid[row+1][col+2]
            return ans
            


        maxii=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                maxii=max(maxii,sums(i,j))
        return maxii
