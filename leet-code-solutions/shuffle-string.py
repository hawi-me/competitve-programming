from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dec = dict()
        for i in range(len(s)):
            dec[indices[i]] = s[i]
        return ''.join(dec[i] for i in range(len(s)))
