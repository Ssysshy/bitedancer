class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
      low = [ [0 for _ in range(9)] for _ in range(9)]
      col = [ [0 for _ in range(9)] for _ in range(9)]
      subbox = [ [ [ 0 for _ in range(9) ] for _ in range(3) ] for _ in range(3) ]
      for i in range(9):
        for j in range(9):
          c = board[i][j]
          if c != '.':
            index = ord(c) - ord('0') - 1
            low[i][index] += 1
            col[j][index] += 1
            subbox[i // 3][j // 3][index] += 1
            if low[i][index] > 1 or col[j][index] > 1 or subbox[i // 3][j // 3][index] > 1:
              return False

      return True

sudoko = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solution = Solution()
print(solution.isValidSudoku(sudoko))