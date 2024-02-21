class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        j=1
        n=len(s)
        count=n
        for i in range(len(s)):
            if s[i] == '(':
                while j < len(s) and s[j] != ')':
                    j+=1
                if  j < len(s) and s[j] == ')': 
                   count -= 2
                   j+=1
            if i == j:
                j+=1
        return count