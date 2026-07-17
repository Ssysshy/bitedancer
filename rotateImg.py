class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        newMatrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                newMatrix[j][n-i-1] = matrix[i][j]
        
        matrix[:] = newMatrix
        """
        Do not return anything, modify matrix in-place instead.
        """

solution = Solution();
solution.rotate([1,2,3], [4,5,6], [7,8,9])