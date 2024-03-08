class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lis = []
        ans = []
        for num in arr:
            lis.append([num, abs(num - x)])  
        lis.sort(key=lambda y: (y[1], y[0]))  
        for i in range(k):
            ans.append(lis[i][0])
        ans.sort()
        return ans
