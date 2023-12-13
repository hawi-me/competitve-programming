class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j :
                    multiple=(nums[i]-1)*(nums[j]-1)
                    out.append(multiple)
        return max(out)

                
