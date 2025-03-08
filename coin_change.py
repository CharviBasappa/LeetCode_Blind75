from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

# Sample Test Cases
solution = Solution()
print(solution.coinChange([1,2,5], 11))  # Output: 3 (5+5+1)
print(solution.coinChange([2], 3))       # Output: -1
print(solution.coinChange([1], 0))       # Output: 0
print(solution.coinChange([186,419,83,408], 6249))
