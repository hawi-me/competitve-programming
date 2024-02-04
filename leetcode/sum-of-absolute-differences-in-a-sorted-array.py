class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        left=0
        total=sum(nums)
        for i, n in enumerate(nums):
            right=total-n-left
            left_size,right_size=i,len(nums)-i-1
            res.append(left_size*n -left + right-right_size*n)
            left+=n
        return res