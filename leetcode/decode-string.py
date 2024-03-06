class Solution:
    def decodeString(self, s: str) -> str:
        
        def split(string):
            new = ''
            i=0
            while i < len(string):
                if string[i].isdigit():
                    digit = 0
                    extracted = ''
                    while string[i].isdigit():
                        digit *= 10
                        digit += int(string[i])
                        i += 1
                    open = 1
                    close = 0
                    i += 1
                    while close != open:
                        extracted += string[i]
                        if string[i] == '[':
                            open += 1
                        if string[i] == ']':
                            close += 1
                        i += 1
                        if close == open: break
                    new += digit * split(extracted)
                else:
                    new += string[i]
                    i += 1
            return new
        return ''.join(split(s).split(']'))