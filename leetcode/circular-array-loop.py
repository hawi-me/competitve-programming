class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        cycle_check = set()
        for i in range(n):
            if i not in  cycle_check:
                cycle_set = set()
                while True:
                    if i in cycle_set:
                        return True
                    cycle_check.add(i)
                    cycle_set.add(i)
                    p , i = i , (i+nums[i])%n
                    
                    if p == i:
                        break
                    if nums[p] > 0 != nums[i] < 0 :
                        break
        return False
                    