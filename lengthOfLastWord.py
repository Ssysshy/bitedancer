class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        slen = s.strip().split(' ')
        # seen = set()
        sslen = [x for x in slen if not (x == '')];
        return len(sslen[len(sslen) - 1])
            




a = 'wood hello     wood'
solution = Solution()
print(solution.lengthOfLastWord(a))
    