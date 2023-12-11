class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        change = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if change:
                    return False
                if i == 1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                change = True
        return True

        

