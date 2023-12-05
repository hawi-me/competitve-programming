class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        strs1=""
        strs2=""
        for i in range(len(word1)):
            strs1 += word1[i]
        for j in range(len(word2)):
            strs2 += word2[j]
        if strs1 == strs2:
            return True
        else:
            return False