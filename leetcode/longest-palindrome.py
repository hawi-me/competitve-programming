class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        count = 0
        odd=False
        if len(s) == 1:
            return 1
        for v in c.values():
            if v % 2 == 1:
                count += v - 1
                odd = True
            else:
                count += v 
        if odd:
            count += 1   
        return count 