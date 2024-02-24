class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for p in s:
            if p == '(':
                stack.append('(')
            else:
                if stack and stack[-1] == '(':
                    cur =stack.pop()
                    stack.append(1)
                else:
                    score=0
                    while stack[-1] != '(':
                        score += stack.pop()
                    stack.pop() 
                    add = score * 2
                    stack.append(add)
        return sum(stack)
        