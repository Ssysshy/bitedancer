class Solution:

    def get_next(self, p: str) -> list:
        n = len(p)
        next_arr = [0] * n
        i = 1
        j = 0

        while i < n:
            if p[i] == p[j]:
                j += 1
                next_arr[i] = j
                i += 1
            else:
                if j != 0:
                    j = next_arr[j - 1]
                else:
                    next_arr[i] = 0
                    i += 1
        
        return next_arr


    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0;
        n = len(haystack)
        m = len(needle)
        next_arr = self.get_next(needle)
        i = 0
        j = 0
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == m:
                return i - j
            elif i < n and haystack[i] != needle[j]:
                if j != 0:
                    j = next_arr[j - 1]
                else:
                    i += 1
        return -1

solution = Solution()
print(solution.strStr('leetcode', 'leeto'))