class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def check(mid):
            summ = 0
            for i in range(len(nums)):   
                summ += ceil(nums[i]/mid)
            return summ <= threshold
        l = 1
        h = max(nums)
        while l <= h:
            mid = (l + h)//2
            if check(mid):
                h = mid - 1
            else:
                l = mid + 1
        return l  
        

        