class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start, end = 0, 0
        ans = 0
        ooc = set()
        
        while end < n:
          while s[end] in ooc:
            ooc.remove(s[start])
            start += 1
          ooc.add(s[end])
          end += 1
          ans = max(ans, end - start)
        
        return ans


solution = Solution()
print(solution.lengthOfLongestSubstring('pwwkew'))