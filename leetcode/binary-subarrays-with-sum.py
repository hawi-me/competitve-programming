class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        Map={0:1}
        count=0
        su=0
        for num in nums:
                su+=num
                if su-goal in Map:
                    count+=Map[su-goal]
                Map[su]=Map.get(su,0)+1
        return count