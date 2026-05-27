class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    arr = sorted(nums)
    n = len(arr)
    i = 0
    ans = []
    while i < n - 1:
      l = i + 1
      r = n - 1
      if i > 0 and arr[i] == arr[i - 1]:
        i += 1
        continue
      while l < r:
        if arr[i] + arr[l] + arr[r] == 0:
          ans.append([arr[i], arr[l], arr[r]])
          while l < r and arr[l] == arr[l + 1]:
            l += 1
          while l < r and arr[r] == arr[r - 1]:
            r -= 1
          l += 1
          r -= 1
        elif arr[i] + arr[l] + arr[r] < 0:
          l += 1
        else:
          r -= 1
      i += 1
    return ans

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))