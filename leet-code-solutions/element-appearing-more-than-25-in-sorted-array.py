class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
     
        c = Counter(arr)
        n = len(arr)
        for key, val in c.items():
            if val > n/4:
                return key

        