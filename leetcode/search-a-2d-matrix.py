class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            start , end = 0 , len(matrix[0]) - 1
            while start <= end:
                mid = (start + end ) // 2
                if matrix[i][mid] > target:
                    end = mid - 1
                elif matrix[i][mid] < target:
                    start = mid + 1
                else:
                    return True
            i+=1
        return False
        



        