class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dictt={}
        output=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i + j
                if key not in dictt:
                    dictt[key] = []
                dictt[key].append(mat[i][j])
        print(dictt)
        for key , val in dictt.items():
            if key % 2 == 0:
                output.extend(dictt[key][::-1])
            else:
                output.extend(dictt[key])

        return output
                
        