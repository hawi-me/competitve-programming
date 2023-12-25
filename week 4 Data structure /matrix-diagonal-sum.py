class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        main = defaultdict(int)
        sum_diag = 0
        sum_rev_diag = 0
        n = len(mat)
        common = 0
        for i in range(n):
                sum_diag += mat[i][i]
                sum_rev_diag += mat[i][n - 1 - i]
                if n % 2 != 0 and i == n // 2:
                    common=mat[i][i]
        return sum_diag + sum_rev_diag - common

