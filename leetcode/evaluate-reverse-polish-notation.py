class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["/", "*", "+", "-"])
        
        for token in tokens:
            if token in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                
                if token == "/":
                    stack.append(int(val2 / val1))
                elif token == "*":
                    stack.append(int(val2 * val1))
                elif token == "+":
                    stack.append(int(val2 + val1))
                else:
                    stack.append(int(val2 - val1))
            else:
                stack.append(int(token))
        
        return stack.pop()   