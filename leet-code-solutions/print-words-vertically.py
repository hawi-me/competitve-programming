class Solution:
    def printVertically(self, s: str) -> List[str]:
         sp=s.split()
         ans= []
         maxlength = max(len(word) for word in sp)
         for i in  range(maxlength):
            vertical=[]
            for word in sp:
                if len(word) > i:
                    vertical.append(word[i])
                else:
                    vertical.append(" ")
            ans.append(vertical)

         finall = []
         for vertical in ans:
            finall.append(''.join(vertical).rstrip())
         return finall
        
                 