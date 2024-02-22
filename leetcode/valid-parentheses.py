class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for par in s:
           
            if par == '{' or par == '[' or par == '(':
                stack.append(par)
            elif len(stack) == 0:
                stack.append(par)
            
            else:
                top = stack[-1]
                if par == ']'  and top == '[' or par == '}' and top == '{' or par == ')' and top == '(':
                  stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        return False
        