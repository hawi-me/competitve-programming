class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = ''.join(str(num) for num in digits)
        summ = int(j) + 1
        ans = []
        while summ > 0:
            r = summ % 10
            summ //= 10
            ans.append(r)
        return ans[::-1]
            




        