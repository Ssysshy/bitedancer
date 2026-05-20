class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(x for x in s.lower() if x.isalnum())
        print(ss, 'ss')

        n = len(ss)
        l = 0
        r = n - 1
        while l < r:
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1
                
        return True

solution = Solution()
print(solution.isPalindrome('0P'))