class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r, c = 0, 0
        m = len(matrix[0]) - 1
        n = len(matrix) - 1
        while r < n:
            c = 0
            while c < m:
                if matrix[r + 1][c + 1] != matrix[r][c]:
                    return False
                c += 1
            r += 1
        return True
                