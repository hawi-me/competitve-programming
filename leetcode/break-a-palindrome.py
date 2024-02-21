class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        pal=list(palindrome)
        n=len(palindrome)
        if len(palindrome) == 1:
            return ""
        for i in range(len(pal)):
            if pal[i] != 'a':
                if len(palindrome) % 2 == 1 and n// 2  == i:
                    continue
                pal[i] = 'a'
                break 
        else:
            pal[-1] = 'b'

        s=''.join(pal)
        return s