from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
            
        return max_profit

# Sample Test Cases
solution = Solution()

prices1 = [7,1,5,3,6,4]
print(solution.maxProfit(prices1))  # Output: 5 (Buy at 1, Sell at 6)

prices2 = [7,6,4,3,1]
print(solution.maxProfit(prices2))  # Output: 0 (No profitable transactions)

prices3 = [2,4,1]
print(solution.maxProfit(prices3))  # Output: 2 (Buy at 2, Sell at 4)

prices4 = [3,2,6,5,0,3]
print(solution.maxProfit(prices4))  # Output: 4 (Buy at 2, Sell at 6)

prices5 = [1,2,3,4,5]
print(solution.maxProfit(prices5))  # Output: 4 (Buy at 1, Sell at 5)
