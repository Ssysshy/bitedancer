class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()
        plen = len(pattern)
        slen = len(ss)
        if plen != slen:
            return False
        
        p2s = dict()
        s2p = dict()

        for i in range(plen):
            x = pattern[i]
            y = ss[i]

            if ((x in p2s and p2s[x] != y) or (y in s2p and s2p[y] != x)):
                return False
            
            p2s[x] = y
            s2p[y] = x
        
        return True

solution = Solution()
print(solution.wordPattern("abba", "dog cat cat dog"))