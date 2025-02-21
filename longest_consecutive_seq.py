from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    

# Sample Test Cases
sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
print(sol.longestConsecutive([1,0,1,2]))  # Output: 3
        