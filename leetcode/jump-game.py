class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        step=nums[0]
        if n == 1:
            return True
        for i in range(len(nums)):
            step=max(step,nums[i] + i)
            if step + 1  >= n:
                return True
            if step == i:
                return False
e