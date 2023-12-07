class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
           sets= set()
           for r in ranges:
               for j in range(r[0],r[1]+1):
                 sets.add(j)
           for l in range(left,right+1):
                if(l not in sets):
                  return False
           return True

                 
          
