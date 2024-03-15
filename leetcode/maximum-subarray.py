class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result=nums[0]
        cur_sum=0
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            result=max(result,cur_sum)
        return result 
        
        