class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(mid):
            hour = 0
            for i in range(len(piles)):
                hour += ceil(piles[i] / mid)
                if hour > h:
                    return False
            return True
        l= 1
        high=max(piles) 
        while l <= high:
            mid = (l + high)//2
            if check(mid):
                high = mid - 1
            else:
                l = mid + 1
        return l

        