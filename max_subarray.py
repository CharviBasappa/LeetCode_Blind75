from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# Sample test cases
solution = Solution()

nums1 = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums1))  # Output: 6

nums2 = [1]
print(solution.maxSubArray(nums2))  # Output: 1

nums3 = [5,4,-1,7,8]
print(solution.maxSubArray(nums3))  # Output: 23

nums4 = [-3, -2, -1, -5]
print(solution.maxSubArray(nums4))  # Output: -1

nums5 = [-5]
print(solution.maxSubArray(nums5))  # Output: -5
