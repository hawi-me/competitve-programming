class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
      
        n=len(costs)//2
        res=0
        s=sorted(costs , key = lambda costs : (costs[0]-costs[1]))
        for i in range(n):
            res+= s[i][0] + s[i+n][1]
        return res