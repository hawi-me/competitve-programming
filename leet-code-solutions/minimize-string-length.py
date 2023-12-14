class Solution:
    def minimizedStringLength(self, s: str) -> int:
        unique_chars = set()
        n = len(s)
        for char in s:
            if char in unique_chars:
                n -= 1
            else:
                unique_chars.add(char)
        return len(unique_chars)

        