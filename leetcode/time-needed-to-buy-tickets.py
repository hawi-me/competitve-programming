class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue= deque()
        for i in range(len(tickets)):
            queue.append((tickets[i],i))

        t = tickets[k] 
        count = 0
        while t != 0:
            num,ind =queue.popleft()
            if ind == k :
                t-=1
            num -= 1
            if num > 0:
              queue.append((num , ind))
            count +=1
        return count 
            
