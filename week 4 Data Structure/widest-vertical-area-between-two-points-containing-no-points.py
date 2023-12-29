class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        out=[]
        ans=[]
        for p in points :
            ans.append(p[0]) 
        ans.sort()
        for i in range(1,len(ans)):
            out.append(ans[i]-ans[i-1])    
        return max(out)
        