class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(x , n):
            if n == 0:
                return 1
            val = p(x , n // 2)
            if n % 2 == 0:
                ans = val * val
            else:
                ans = val*val*x
            return ans
        ans = p(x , abs(n))
        if n  > 0:
            return ans
        else:
            return 1/ans

        