class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False

        t2s = dict()
        s2t = dict()

        for i in range(slen):
            x = s[i]
            y = t[i]

            if ((x in s2t and s2t[x] != y) or (y in t2s and t2s[y] != x)):
                return False

            s2t[x] = y
            t2s[y] = x

        return True

solution = Solution()
print(solution.isIsomorphic("egg", "add"))