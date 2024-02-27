class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue=deque()
        deck.sort(reverse = True)
        for i in range(len(deck)):
            if len(queue) > 1 :
                k=queue.pop()
                queue.appendleft(k)
            queue.appendleft(deck[i])
        return queue
        


        