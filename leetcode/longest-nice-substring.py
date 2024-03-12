class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
           return ""
        strs_set = set(s)
        for i, chars in enumerate(s):
           if chars.swapcase() not in strs_set:
               strs1 = self.longestNiceSubstring(s[0:i])
               strs2 = self.longestNiceSubstring(s[i+1:])
               return strs2 if len(strs2) > len(strs1) else strs1
        return s
        