class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
    

s = Solution()

print(s.uniquePaths(3, 7))  # Output: 28
print(s.uniquePaths(3, 2))  # Output: 3
print(s.uniquePaths(1, 1))  # Output: 1
print(s.uniquePaths(10, 10))  # Output: 48620