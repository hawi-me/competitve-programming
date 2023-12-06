class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        res=[]
        for word in words:
               word_lower = word.lower()
               if all(char in row1 for char in word_lower):
                  res.append(word)
               elif all(char in row2 for char in word_lower):
                  res.append(word)
               elif all(char in row3 for char in word_lower):
                  res.append(word)
               
        return res
        

                  
                  
                  
                
                   
