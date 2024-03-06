class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums) - 1
        minm = float('inf')
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h= mid - 1
                minm = min(minm,nums[mid])
        return minm