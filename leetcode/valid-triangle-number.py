class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        valid = 0
        for last in range(len(nums) -1 ,-1,-1):
            l=0
            r=last-1
            while r > l :
                if  nums[l] + nums[r] > nums[last]:
                    valid += r-l
                    r -= 1
                else:
                    l+=1
        return valid