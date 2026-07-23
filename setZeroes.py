class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix) # 行
        cols = len(matrix[0]) # 列 一般先循环这个
        setted = [[False] * cols for _ in range(rows)] # 记录是否设置为0
        rows0 = set()
        cols0 = set()
        print(setted, 'setted')
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if j not in cols0:
                        cols0.add(j)
                    if i not in rows0:
                        rows0.add(i)
        
        for i in range(rows):
            for j in range(cols):
                if j in cols0 or i in rows0:
                    matrix[i][j] = 0
        

        print(matrix, 'matrix')
        """
        Do not return anything, modify matrix in-place instead.
        """

solution = Solution()
print(solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))