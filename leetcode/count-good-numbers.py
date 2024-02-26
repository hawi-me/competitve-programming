class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def p(x , n, mod):
            if n == 0:
                return 1
            val = p(x , n // 2, mod)
            if n % 2 == 0:
                ans = val * val
            else:
                ans = val * val * x
            return ans % mod
        
        mod = 10**9 + 7
        if n == 1:
            return 5
        if n % 2 != 0:
            return p(5, (n + 1) // 2, mod) * p(4, n // 2, mod) % mod
        else:
            return p(5, n // 2, mod) * p(4, n // 2, mod) % mod
