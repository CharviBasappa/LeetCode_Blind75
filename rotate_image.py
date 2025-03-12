from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the given n x n matrix by 90 degrees clockwise in place.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

# Sample Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    solution.rotate(matrix1)
    print("Rotated Matrix 1:")
    for row in matrix1:
        print(row)

    # Test Case 2
    matrix2 = [[5, 1, 9, 11],
               [2, 4, 8, 10],
               [13, 3, 6, 7],
               [15, 14, 12, 16]]
    solution.rotate(matrix2)
    print("\nRotated Matrix 2:")
    for row in matrix2:
        print(row)

    # Test Case 3 (Single element)
    matrix3 = [[1]]
    solution.rotate(matrix3)
    print("\nRotated Matrix 3:")
    for row in matrix3:
        print(row)

    # Test Case 4 (2x2 Matrix)
    matrix4 = [[1, 2],
               [3, 4]]
    solution.rotate(matrix4)
    print("\nRotated Matrix 4:")
    for row in matrix4:
        print(row)
