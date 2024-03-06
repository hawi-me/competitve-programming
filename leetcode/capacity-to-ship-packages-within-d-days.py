class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            summ = 0
            d=1
            for i in range(len(weights)):
                if summ + weights[i] > mid:
                    d += 1
                    summ = weights[i]
                else:
                    summ += weights[i]
                if d > days:
                    return False
            return True
        l = max(weights)
        h = sum(weights)
        while l <= h:
            mid = (l + h) // 2
            if check(mid):
                h = mid - 1
            else:
                l = mid + 1
        return l



        
        