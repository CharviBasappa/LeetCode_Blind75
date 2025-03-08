class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n

        first, second = 1, 2
        for _ in range(3, n+1):
            first, second = second, first + second

        return second
    
# Sample Test Cases
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(5))  # Output: 8
print(solution.climbStairs(10)) # Output: 89



















# class Solution:
#     def climbStairs(self, n: int) -> int:
#         def findWays(steps, path):
#             if steps == n:
#                 ways.append(path[:])
#                 return
#             if steps + 1 <= n:
#                 findWays(steps + 1, path + [1])
#             if steps + 2 <= n:
#                 findWays(steps + 2, path + [2])
#         ways = []
#         findWays(0, [])
#         for i, way in enumerate(ways, 1):
#             print(f"{i}. {' + '.join(map(str, way))}")
#         return len(ways)

# # Sample Test Cases with Explanation
# solution = Solution()
# print("\nWays to climb 2 steps:")
# print("Total ways:", solution.climbStairs(2))  # Output: 2

# print("\nWays to climb 3 steps:")
# print("Total ways:", solution.climbStairs(3))  # Output: 3

# print("\nWays to climb 4 steps:")
# print("Total ways:", solution.climbStairs(4))  # Output: 5

# print("\nWays to climb 5 steps:")
# print("Total ways:", solution.climbStairs(5))  # Output: 8
