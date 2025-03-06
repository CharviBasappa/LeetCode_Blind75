from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
    
# Sample Test Cases
solution = Solution()

# Test Case 1: Array is rotated at index 3
print(solution.findMin([3, 4, 5, 1, 2]))  # Output: 1

# Test Case 2: Array is rotated at index 4
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0

# Test Case 3: No rotation (already sorted)
print(solution.findMin([11, 13, 15, 17]))  # Output: 11

# Test Case 4: Rotated at last element
print(solution.findMin([2, 3, 4, 5, 6, 7, 8, 1]))  # Output: 1

# Test Case 5: Only one element in the array
print(solution.findMin([1]))  # Output: 1

# Test Case 6: Array rotated multiple times
print(solution.findMin([7, 8, 9, 1, 2, 3, 4, 5, 6]))  # Output: 1

# Test Case 7: Another variation with different numbers
print(solution.findMin([10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 1