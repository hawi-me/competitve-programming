class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        subarrays = []
        s= set(nums)
        count=0
        for i in range(len(nums)):
            subarray=set()
            for j in range(i ,len(nums)):
                subarray.add(nums[j]) 
                if len(subarray) == len(s):
                    count+=1
                elif  len(subarray) > len(s):
                    break
        return count
        