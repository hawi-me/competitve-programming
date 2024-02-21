class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        step=0
        rem=0
        while target > 1:
            if maxDoubles > 0:
                if target % 2 != 0:
                    step+=1
                    rem+=1
                else: 
                    step+=1
                target= target//2
                maxDoubles-=1
            else:
                    step += (target - 1)
                    break
        return step + rem
        
            
