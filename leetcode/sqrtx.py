class Solution:
    def mySqrt(self, x: int) -> int:
        l =0
        h = x
        ans=0
        while l <= h:
            mid = (l + h) // 2
            if mid ** 2 > x:
                h = mid - 1
            elif mid ** 2 < x:
                l = mid + 1
                ans = mid
            else:
                return mid
        return ans
                   