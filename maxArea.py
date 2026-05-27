class Solution:
  def maxArea(self, height):
    l, r = 0, len(height) - 1
    max = 0
    while l <= r:
      area = min(height[l], height[r]) * (r - l)
      if area > max:
        max = area
      if height[l] <= height[r]:
        l += 1
      else:
        r -= 1
    return max

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))