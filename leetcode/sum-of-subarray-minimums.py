class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans=0
        stack=[-1]
        res=0
        arr.append(float("-inf"))
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                    ind= stack.pop()
                    cur = stack[-1]
                    left=ind - cur
                    right = i - ind
                    res += arr[ind]*left*right
            stack.append(i)
        return res % (10 ** 9 + 7) 
            
                    