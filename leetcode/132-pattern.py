class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        flag = False
        nextg=[-1]*len(nums)
        minmum=[0]*len(nums)
        for i in range(len(nums)- 1 , -1 , -1 ):
            while stack and nums[stack[-1]] < nums[i]:
                k=stack.pop()
                nextg[k] = i
            stack.append(i)
        minimum_so_far = float('inf')
        previous_minimums = [float('inf')] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                previous_minimums[i] = minimum_so_far 
                minimum_so_far = nums[i]  
            else:
                if nums[i] < minimum_so_far:
                    minimum_so_far = nums[i]
                previous_minimums[i] = minimum_so_far
        for i in range(len(nums)- 1 , -1 , -1 ):            
            if nextg[i] != -1 and  previous_minimums[nextg[i]] < nums[i]:
                return True
        else: 
            return False
       
       
        