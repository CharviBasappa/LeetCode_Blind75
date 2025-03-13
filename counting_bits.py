from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # Right shift to remove last bit + check if last bit is 1
        return ans

# Sample test cases
solution = Solution()
print(solution.countBits(2))  # Output: [0, 1, 1]
print(solution.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
print(solution.countBits(10)) # Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
