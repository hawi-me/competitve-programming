class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for i in range(len(matrix[0])):
            transposed_row = []
            for j in range(len(matrix)):
                transposed_row.append(matrix[j][i])
            transposed.append(transposed_row)
        return transposed


        