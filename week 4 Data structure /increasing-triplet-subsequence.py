class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m1=float('inf')
        m2=float('inf')
        for n in nums:
            if n > m2:
                return True
            elif n <= m1:
                m1= min(m1,n)
            elif n <= m2:
                m2= min(m2,n)
        return False
            

