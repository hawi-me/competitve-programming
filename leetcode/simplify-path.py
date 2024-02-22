class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        res="/"
        splitedpath = path.split('/')
        print(splitedpath)
        for p in splitedpath:
            if len(stack) != 0 and p == '..' :
                stack.pop()
            elif p != ''  and  p != '.' and p != '..':
                stack.append(p)   
        print(stack)
        res += "/".join(stack)
        return res