from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable, prev_height):
            if (r, c) in reachable or r < 0 or r >= m or c < 0 or c >= n or heights[r][c] < prev_height:
                return
            reachable.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc, reachable, heights[r][c])

        for i in range(m):
            dfs(i, 0, pacific_reachable, heights[i][0])
            dfs(i, n - 1, atlantic_reachable, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pacific_reachable, heights[0][j])
            dfs(m - 1, j, atlantic_reachable, heights[m - 1][j])

        return list(map(list, pacific_reachable & atlantic_reachable))


# Sample test cases
if __name__ == "__main__":
    solution = Solution()

    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    print(solution.pacificAtlantic(heights1))
    # Expected Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    heights2 = [[1]]
    print(solution.pacificAtlantic(heights2))
    # Expected Output: [[0,0]]
