from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(nums[i], nums[i] * max_product)
            min_product = min(nums[i], nums[i] * min_product)
            
            result = max(result, max_product)

        return result

# Sample Test Cases
solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))  # Output: 6
print(solution.maxProduct([-2, 0, -1]))    # Output: 0
print(solution.maxProduct([1, -2, -3, 4])) # Output: 24
print(solution.maxProduct([-1, -3, -10, 0, 60])) # Output: 60
print(solution.maxProduct([-2, 3, -4]))    # Output: 24
