class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        str = ''
        flag = 1
        aim = 0
        outsideStep = 1
        while aim < numRows:
          inFlag = 1
          insideStep = 1
          for v in s:
            if inFlag == flag:
              str += v
            inFlag += insideStep
            if inFlag == numRows:
              insideStep = -1
            elif inFlag == 1:
              insideStep = 1
          flag += outsideStep
          # 翻转步长
          if flag == numRows:
            outsideStep = -1
          elif flag == 1:
            outsideStep = 1
          aim += 1

        return str


solution = Solution()
print(solution.convert('PAYPALISHIRING', 3))
