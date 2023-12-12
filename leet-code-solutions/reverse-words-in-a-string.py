
        # l= s.split()
        # res=""
        # ans=l[::-1]
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        ans = ""
        for i in range(len(l) - 1, -1, -1):
            ans += l[i] + ' '
        return ans.strip()
