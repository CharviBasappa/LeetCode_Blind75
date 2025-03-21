from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True


# Instantiate the solution class
sol = Solution()

# Test Case 1
nums1 = [2, 3, 1, 1, 4]
print(sol.canJump(nums1))  # Output: True

# Test Case 2
nums2 = [3, 2, 1, 0, 4]
print(sol.canJump(nums2))  # Output: False

# Test Case 3 - Single element (already at last index)
nums3 = [0]
print(sol.canJump(nums3))  # Output: True

# Test Case 4 - Large jump at start
nums4 = [5, 0, 0, 0, 0, 0]
print(sol.canJump(nums4))  # Output: True

# Test Case 5 - All zeros except first
nums5 = [1, 0, 0]
print(sol.canJump(nums5))  # Output: False
