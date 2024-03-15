class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        prefix_sum =[0]*(n + 1)
        for start , end in requests:
            prefix_sum[start] += 1
            prefix_sum[end + 1] -= 1
        for i in range(1,n + 1):
            prefix_sum[i] += prefix_sum[i-1]
        nums.sort()
        prefix_sum.pop()
        prefix_sum.sort()
        max_sum = 0
        m = 10**9 + 7
        for i in range(n):
            max_sum += prefix_sum[i]*nums[i]
        return max_sum % m
        
