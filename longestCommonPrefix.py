class Solution:
  def longestCommonPrefix(self, strs):
    if not strs:
      return ''
    
    base = strs[0]
    for s in strs[1:]:
      while not s.startwith(base):
        base = base[:-1]
        if not base:
          return ''

    return base

solution = Solution()
print(solution.longestCommonPrefix(['flower','flow','flight']))
