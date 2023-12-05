class Solution:
    def freqAlphabets(self, s: str) -> str:
        dictionary = {}
        res = []
        for i in range(1, 10):
            dictionary[str(i)] = chr(ord('a') + i - 1)
            print(dictionary)
        for i in range(10, 27):
            dictionary[str(i) + '#'] = chr(ord('a') + i - 1)
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                res.append(dictionary[s[i:i + 3]])
                i += 3
            else:
                res.append(dictionary[s[i]])
                i += 1
        return ''.join(res)
