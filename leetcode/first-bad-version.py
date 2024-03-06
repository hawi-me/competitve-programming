# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # for i in range(n + 1):
        #     if isBadVersion(i):
        #         return i
        l , h = 1 , n
        ans = 0
        while l <= h:
            mid = (l + h) // 2
            if isBadVersion(mid):
                ans = mid
                h = mid - 1
            else:
               l = mid + 1
        return ans
            

            
        