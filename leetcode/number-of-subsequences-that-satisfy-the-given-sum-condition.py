class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
    
        count = 0
        for i in range(len(nums)):
            num = target - nums[i]
            if nums[i] <= num:
                ind = bisect_right(nums, num)
                n= ind - i - 1
                count += 2 ** n
        
        return count % (( 10 ** 9) + 7)
               