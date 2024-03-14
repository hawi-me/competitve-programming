class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] =  nums[i] + prefix_sum[i-1]
        dictt = {}
        res=inf
        summ=sum(nums) 
        total= (summ % p)
        dictt[total] = 0
        if total == 0:
            return 0
        if summ < p:
            return -1
        for i in range(len(prefix_sum)):
            m=(prefix_sum[i] % p) 
            if m in dictt:
                res = min(res, ((i + 1 )-dictt[m]))
            t = (m + total)%p
            dictt[t] = (i + 1)
        if res == len(nums):
            return -1
        
        return res if res != inf else -1 

        
        