class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if i*2 < len(nums): 
                freq = nums[i*2]
                val= nums[2*i+1]
                res.extend([val]*freq)
        return res
                
