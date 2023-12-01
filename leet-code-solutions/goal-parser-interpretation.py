class Solution:
    def interpret(self, command: str) -> str:
        strs = ""
        i = 0
        while ( i < len(command)):
            if(command[i] == 'G'):
                strs += 'G'
                i += 1
            elif command[i:i+2] == '()':
                strs += 'o'
                i += 2
            elif command[i:i+4] == '(al)':
                strs += 'al'
                i += 4
            else:
             i += 1
        return strs