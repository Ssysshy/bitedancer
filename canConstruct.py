import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteLen = len(ransomNote)
        for i in range(ransomNoteLen):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i], "", 1)
            else:
                return False
        return True

    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not (collections.Counter(ransomNote) - collections.Counter(magazine))
solution = Solution()
print(solution.canConstruct1('aa', 'aab'))
