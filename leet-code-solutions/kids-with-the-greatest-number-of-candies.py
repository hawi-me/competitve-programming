class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = list()
        for i in range(len(candies)):
            sum = candies[i] + extraCandies 
            if sum >= m :
                res.append(True)
            else:
                res.append(False)
        return res
            
            