class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j= 0 #left pointer
        #right pointer
        Map = defaultdict(int)
        largest = 0
        for i in range(len(s)):
            Map[s[i]] += 1
            while (i-j+1) - max(Map.values()) > k:
                Map[s[j]] -=1
                j+=1
            largest = max(largest,i-j+1)
        return largest

       