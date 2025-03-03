from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Test Cases
sol = Solution()
print(sol.missingNumber([3, 0, 1]))  # Output: 2
print(sol.missingNumber([0, 1]))  # Output: 2
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8
print(sol.missingNumber([0]))  # Output: 1
print(sol.missingNumber([1]))  # Output: 0
print(sol.missingNumber([0, 2, 3, 4]))  # Output: 1
print(sol.missingNumber([0, 1, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 2
print(sol.missingNumber([5, 3, 0, 1, 2]))  # Output: 4