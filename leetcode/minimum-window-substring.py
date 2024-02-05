class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        count_sub = {}
        countT=Counter(t) 
        have , need = 0 , len(countT)
        res, reslen=[-1,-1] , float("inf")
        l=0
        for r in range(len(s)):
            c=s[r]
            count_sub[c] = 1 +count_sub.get(c,0)
            if c in countT and count_sub[c] == countT[c]:
                have+=1
            while have == need:
                #update result
                if (r-l+1) < reslen:
                    res=[l,r]
                    reslen = (r-l+1)
                count_sub[s[l]]-=1
                if s[l] in countT and count_sub[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""
        
        