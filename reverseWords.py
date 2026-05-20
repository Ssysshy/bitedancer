class Solution:
  def reverseWords(self, s: str) -> str:
    s = s.strip()
    sa = [x for x in s.split(' ') if x]
    left = 0
    right = len(sa) - 1
    d = []
    while(left <= right):
      d.append(sa[right])
      right -= 1
    
    return ' '.join(d)

solution = Solution()
print(solution.reverseWords("a good   example"))
