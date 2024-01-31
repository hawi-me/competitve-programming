class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        stack = []  
        result = 0
        
        for i, val in enumerate(arr):
            while stack and val < arr[stack[-1]]:
                j = stack.pop()  
                k = stack[-1] if stack else -1 
                result += arr[j] * (i - j) * (j - k) % MOD 
                result %= MOD

            stack.append(i)
        
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result += arr[j] * (len(arr) - j) * (j - k) % MOD
            result %= MOD

        return result
