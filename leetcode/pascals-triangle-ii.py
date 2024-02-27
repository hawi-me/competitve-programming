class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex-1)
        new=[1]*(rowIndex + 1) 
        for i in range(1,len(new) -1):
            new[i] = prev[i] + prev[i - 1]
        return new  

        