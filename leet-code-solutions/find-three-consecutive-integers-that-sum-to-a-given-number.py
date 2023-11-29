class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        result = []
        hold=num-3
        first= hold/3
        second=first+1
        third= first+2
        if(hold % 3 != 0 ):
         return result
        else:
        
         result.append(int(first))
         result.append(int(second))
         result.append(int(third))
        return result
