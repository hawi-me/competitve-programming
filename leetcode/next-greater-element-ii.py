class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        stack = []
        n = len(nums)
        for i in range(len(nums)*2) :
            while stack and nums[stack[-1]] < nums[i % n]:
                k = stack.pop()
                res[k] = nums[ i % n]
            if i < n :
                stack.append( i)   
        return res
        