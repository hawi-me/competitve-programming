class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        j = 0  # Index for spaces list
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                res += ' '
                j += 1  
            res += s[i]
        return res

        







        
        