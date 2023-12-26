class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_1 = sum(nums)
        count_zeros = 0
        div_sum = [count_1+count_zeros]

        for i in range(n):
            if nums[i] == 0:
                count_zeros += 1
            if nums[i] == 1:
                count_zeros -= 1
            div_sum.append(count_1 + count_zeros)
        print(div_sum)

        max_score = max(div_sum)
        max_indices = [key for key, val in enumerate(div_sum) if val == max_score]

        return max_indices


        
            

        