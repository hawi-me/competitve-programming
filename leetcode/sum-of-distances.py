class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dictt=defaultdict(list)
        ans=[0]*len(nums)
        for i in range(len(nums)):
            dictt[nums[i]].append(i)
        for k , v in dictt.items():
            suf_sum = sum(v)
            prefix_sum=0
            l=len(v)
            pre=0
            for i in v:
                prefix_sum+=i
                pre+=1
                suf_sum-=i
                l-=1
                ans[i] = -prefix_sum + pre*i - l*i + suf_sum
        return ans