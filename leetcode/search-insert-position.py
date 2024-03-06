class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j = bisect_left(nums, target)
        if j < len(nums):
            return j
        else:
           return len(nums)
        