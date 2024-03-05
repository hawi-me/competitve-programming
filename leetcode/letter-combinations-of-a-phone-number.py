class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictt={'2' : ['a','b','c'], '3' : ['d' ,'e','f'] , '4' : ['g','h','i'] , '5' : ['j','k','l'] , '6' : ['m','n','o'] , '7' : ['p','q','r','s'], '8' : ['t','u','v'] , '9' :['w','x','y','z']}
        total=""
        ans=[]
        for  n in digits:
           total += ''.join(dictt[n])
        if len(digits) == 0:
            return []
            
        def backtrack(i, path,total):
            if len(path) == len(digits):
                ans.append(''.join(path[:]))
                return
            for j in range(i,len(total)):
                length = len(path)
                if total[j] not in dictt[digits[length]]:
                    continue
                path.append(total[j])
                backtrack(j+1,path,total)
                path.pop()
        backtrack(0,[],total)
        return set(ans)
            
