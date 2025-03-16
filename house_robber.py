# from typing import List

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]

#         prev1, prev2 = 0, 0

#         for num in nums:
#             temp = max(prev1, prev2 + num)
#             prev2 = prev1
#             prev1 = temp

#         return prev1

# # Sample test cases
# if __name__ == "__main__":
#     solution = Solution()
    
#     # Test case 1
#     nums1 = [1, 2, 3, 1]
#     print(f"Test Case 1: {solution.rob(nums1)}")  # Expected output: 4

#     # Test case 2
#     nums2 = [2, 7, 9, 3, 1]
#     print(f"Test Case 2: {solution.rob(nums2)}")  # Expected output: 12

#     # Test case 3 (Edge case: only one house)
#     nums3 = [10]
#     print(f"Test Case 3: {solution.rob(nums3)}")  # Expected output: 10

#     # Test case 4 (Edge case: all zeroes)
#     nums4 = [0, 0, 0, 0, 0]
#     print(f"Test Case 4: {solution.rob(nums4)}")  # Expected output: 0

#     # Test case 5 (Increasing values)
#     nums5 = [1, 3, 1, 3, 100]
#     print(f"Test Case 5: {solution.rob(nums5)}")  # Expected output: 103




from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0, []
        if len(nums) == 1: return nums[0], [0]

        dp, robbed = [0] * len(nums), [[] for _ in range(len(nums))]
        dp[0], robbed[0] = nums[0], [0]
        
        if nums[1] > nums[0]:
            dp[1], robbed[1] = nums[1], [1]
        else:
            dp[1], robbed[1] = nums[0], [0]

        for i in range(2, len(nums)):
            if dp[i-1] > dp[i-2] + nums[i]:
                dp[i], robbed[i] = dp[i-1], robbed[i-1]
            else:
                dp[i], robbed[i] = dp[i-2] + nums[i], robbed[i-2] + [i]

        return dp[-1], robbed[-1]

# Test cases with dynamic explanations
if __name__ == "__main__":
    solution = Solution()
    test_cases = [[1, 2, 3, 1], [2, 7, 9, 3, 1], [10], [0, 0, 0, 0, 0], [1, 3, 1, 3, 100]]

    for nums in test_cases:
        max_money, robbed_indices = solution.rob(nums)
        robbed_houses = [nums[i] for i in robbed_indices]
        print(f"Input: {nums}\nOutput: {max_money}")
        print(f"Explanation: Rob houses at indices {robbed_indices} with money {robbed_houses}.")
        print(f"Total amount you can rob = {' + '.join(map(str, robbed_houses))} = {max_money}.\n")
