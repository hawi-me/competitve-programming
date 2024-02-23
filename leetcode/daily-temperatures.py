class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warm=[0]*len(temperatures)
        stack=[(temperatures[0],0)]
        for i in range(1 ,len(temperatures)):
            while stack and temperatures[stack[-1][1]] < temperatures[i]:
                num , ind = stack.pop()
                warm[ind] = i - ind
            stack.append((temperatures[i], i))
        return warm

        