class TimeMap:

    def __init__(self):
        self.dictt= defaultdict(list)
        self.ans = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictt[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        start = 0 
        end = len(self.dictt[key]) - 1

        while start <= end:
            mid = (start + end ) // 2
            if timestamp > self.dictt[key][mid][1]:
                start = mid + 1
                self.ans.append(self.dictt[key][mid][0])
            elif  timestamp < self.dictt[key][mid][1]:
                end = mid - 1
            else:
                return self.dictt[key][mid][0]
        if len(self.ans) == 0:
            return ""
        else:
            return self.ans[-1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)