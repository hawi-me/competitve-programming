from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        res = []
        for num in nums:
            if num < 0:
                arr2.append(num)
            else:
                arr1.append(num)
        
        for i in range(max(len(arr1), len(arr2))):
            if i < len(arr1):
                res.append(arr1[i])
            if i < len(arr2):
                res.append(arr2[i])

        return res

        

         
