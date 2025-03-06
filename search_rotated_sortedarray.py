from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


# Sample test cases
solution = Solution()

# Test Case 1
nums1 = [4,5,6,7,0,1,2]
target1 = 0
print(solution.search(nums1, target1))  # Output: 4

# Test Case 2
nums2 = [4,5,6,7,0,1,2]
target2 = 3
print(solution.search(nums2, target2))  # Output: -1

# Test Case 3
nums3 = [1]
target3 = 0
print(solution.search(nums3, target3))  # Output: -1

# Test Case 4
nums4 = [5, 6, 7, 8, 9, 1, 2, 3, 4]
target4 = 8
print(solution.search(nums4, target4))  # Output: 3

# Test Case 5
nums5 = [6, 7, 8, 1, 2, 3, 4, 5]
target5 = 1
print(solution.search(nums5, target5))  # Output: 3
