from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs_stack(r, c):
            stack = [(r, c)]
            while stack:
                row, col = stack.pop()
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                    grid[row][col] = "0"
                    stack.append((row + 1, col))
                    stack.append((row - 1, col))
                    stack.append((row, col + 1))
                    stack.append((row, col - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs_stack(r, c)

        return island_count
    
# Sample Test Cases
solution = Solution()

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(solution.numIslands(grid1))  # Output: 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid2))  # Output: 3

grid3 = [
  ["1","0","1","0","1"],
  ["0","1","0","1","0"],
  ["1","0","1","0","1"]
]
print(solution.numIslands(grid3))  # Output: 8

grid4 = [
  ["0","0","0","0"],
  ["0","0","0","0"],
  ["0","0","0","0"]
]
print(solution.numIslands(grid4))  # Output: 0

