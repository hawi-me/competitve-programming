class RecentCounter:

    def __init__(self):
        self.request=deque()
        self.count=0
        
    def ping(self, t: int) -> int:
        self.request.append(t)
        self.count += 1
        while self.request and self.request[0] < t - 3000:
            self.request.popleft()
            self.count -= 1
        return self.count
    

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)