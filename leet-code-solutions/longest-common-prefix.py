class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = "" 
        prefix = sorted(strs)
        begin = prefix[0]
        end = prefix[-1]
        for i in range(min(len(begin),len(end))):
            if(begin[i] != end[i]):
                return result
            result += begin[i]
        return result


