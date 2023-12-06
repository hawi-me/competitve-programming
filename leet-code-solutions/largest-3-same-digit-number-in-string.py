class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest_same = ""
        for i in range(len(num) - 2):
         if num[i] == num[i + 1]== num[i + 2]:
            largest_same = max(largest_same,num[i:i+3])
                        
        return largest_same
