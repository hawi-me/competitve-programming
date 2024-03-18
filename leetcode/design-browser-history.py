class doublyLinked:
    def __init__(self,val,prev=None,next=None):
        self.prev = prev
        self.next = next
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.his = doublyLinked(homepage)

    def visit(self, url: str) -> None:
        self.his.next =  doublyLinked(url,self.his)
        self.his = self.his.next
        

    def back(self, steps: int) -> str:
        while self.his.prev and steps > 0:
            self.his = self.his.prev
            steps -= 1
        return self.his.val

    def forward(self, steps: int) -> str:
        while self.his.next and steps > 0:
            self.his = self.his.next
            steps -= 1
        return self.his.val
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)