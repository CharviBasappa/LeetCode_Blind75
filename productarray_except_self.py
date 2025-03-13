from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

# Sample test cases
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))  # Output: [24, 12, 8, 6]
print(solution.productExceptSelf([-1,1,0,-3,3]))  # Output: [0, 0, 9, 0, 0]
