class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l , h = 0 , len(nums) -1 
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        first , ans = -1 , -1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                first = mid 
                h = mid - 1
            elif nums[mid] < target:
                l = mid  + 1
            else:
                h = mid - 1
        l , h = 0 , len(nums) -1 
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                ans = mid
                l = mid + 1
            elif nums[mid] > target:
                h = mid  - 1
            else:
                l = mid + 1        
        return [first,ans]
        