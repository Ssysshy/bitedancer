class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
          low, high = i + 1, n - 1
          while low <= high:
            mid = (high + low) // 2
            if numbers[mid] + numbers[i] == target:
              return [i + 1, mid + 1]
            elif numbers[mid] + numbers[i] > target:
              high = mid - 1
            else:
              low = mid + 1

        return [-1, -1]
    
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        low = 0
        high = n - 1
        while low <= high:
          if numbers[low] + numbers[high] == target:
            return [low + 1, high + 1]
          elif numbers[low] + numbers[high] < target:
            low += 1
          else:
            high -= 1

        return [-1, -1]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))