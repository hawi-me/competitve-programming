class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(left, right):
            if left == right:
                return nums[left]
                
            score_left = nums[left] - solve(left + 1, right)

            score_right = nums[right] - solve(left, right - 1)

            return max(score_left, score_right)

        player_score = solve(0, len(nums) - 1)

        return player_score >= 0
        