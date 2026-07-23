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
    
    def rotate1(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        
        # 水平对换
        for i in range(n // 2):
            for j in range(n):
                matrix[n - i - 1][j], matrix[i][j] = matrix[i][j], matrix[n - i - 1][j]
        
        # 对角置换
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

solution = Solution();
solution.rotate([1,2,3], [4,5,6], [7,8,9])