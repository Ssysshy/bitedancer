class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1 # 最低长度
        for i in range(n):
          total = 0
          for j in range(i, n):
            total += nums[j]
            if total >= target:
              ans = min(ans, j - i + 1)
              break

        return 0 if ans == n + 1 else ans

    def minSubArrayLenHua(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0

        while end < n:
          total += nums[end]
          while total >= target:
            ans = min(ans, end - start + 1)
            total -= nums[start]
            start += 1

          end += 1

        return 0 if ans == n + 1 else ans


solution = Solution()
solution.minSubArrayLen(7, [2,3,1,2,4,3])