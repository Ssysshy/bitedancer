class Solution:

    SYMBOL_VALUES = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }

    @staticmethod
    def findMaxNumStr(num: int) -> str:
        for k, v in sorted(Solution.SYMBOL_VALUES.items(), key=lambda x: x[1], reverse=True):
            if num >= v:
                return k
        return 'I'

    def intToRoman(self, num):
        str = ''
        n = num
        while n > 0:
            curKey = Solution.findMaxNumStr(n)
            curVal = Solution.SYMBOL_VALUES[curKey]
            str += curKey
            n -= curVal        
        return str
            

solution = Solution()
print(solution.intToRoman(1994))
    