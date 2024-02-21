class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=Counter(answers)
        ans=0
        for n , x in c.items():
            print(c[x])
            ans+= (n + x)//(n+1)*((n+1))
        return ans

        