class Solution:
    def balancedString(self, s: str) -> int:
        n=len(s)//4
        c=Counter(s)
        l=0
        min_len , l = float('inf'),0
        for r in range(len(s)):
            c[s[r]] -= 1
            while l < len(s) and all(c.get(k,0) <= n for k in ['Q','W','E','R']):
                min_len = min(min_len , r-l + 1)
                c[s[l]] += 1
                l+=1
                
                
        return min_len
                



        