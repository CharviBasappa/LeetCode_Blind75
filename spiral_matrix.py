from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# Sample Test Cases
solution = Solution()

# Test Case 1
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.spiralOrder(matrix1))  # Expected Output: [1,2,3,6,9,8,7,4,5]

# Test Case 2
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(solution.spiralOrder(matrix2))  # Expected Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Test Case 3 (Edge Case - Single row)
matrix3 = [[1, 2, 3, 4, 5]]
print(solution.spiralOrder(matrix3))  # Expected Output: [1, 2, 3, 4, 5]

# Test Case 4 (Edge Case - Single column)
matrix4 = [[1], [2], [3], [4]]
print(solution.spiralOrder(matrix4))  # Expected Output: [1, 2, 3, 4]

# Test Case 5 (Edge Case - Single element)
matrix5 = [[42]]
print(solution.spiralOrder(matrix5))  # Expected Output: [42]
