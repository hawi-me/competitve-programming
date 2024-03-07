class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        lis = []
        ans = []
        dictt = {}
        for i in range(len(intervals)):
            lis.append(intervals[i][0])
            dictt[intervals[i][0]] = i
        lis.sort()
        for i in range(len(intervals)):
            ind = bisect_left(lis,intervals[i][1])
            if ind == len(lis):
                ans.append(-1)
            else:
                ans.append(dictt[lis[ind]])
        return ans
        