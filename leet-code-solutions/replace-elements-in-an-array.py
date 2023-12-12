class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dictt = {}
        for i in range(len(nums)):
            dictt[nums[i]] = i
        for op1, op2 in operations:
            nums[dictt[op1]] = op2
            dictt[op2] = dictt[op1]
        return nums


    


           
            
