class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        rs=0
        lis=[]
        for i in range(len(nums)):
            rs+=nums[i]
            n= ceil(rs / (i+1))
            lis.append(n)
        return max(lis)


        