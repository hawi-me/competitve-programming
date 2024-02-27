class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dictt={}
        for i in range(len(s)):
            if s[i] not in dictt:
                dictt[s[i]] = s.rfind(s[i])
        end=dictt[s[0]] 
        newl=[] 
        start=0
        for i in range(len(s)):
            end= max(end,dictt[s[i]])
            if i == end:
                newl.append(end - start+1)
                start=end+1
        return newl
        