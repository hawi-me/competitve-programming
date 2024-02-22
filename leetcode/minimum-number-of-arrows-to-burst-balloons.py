class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow = 1
        s=sorted(points , key= lambda points : points[1] )
        end=s[0][1]
        for  i in range(1,len(s) ):
            if s[i][0] > end:
                arrow +=1
                end=s[i][1]
            
        return arrow
        