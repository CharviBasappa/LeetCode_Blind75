from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0



solution = Solution()

# Test Case 1
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
print("\nTest Case 1:")
print("Input Matrix:")
for row in matrix1:
    print(row)

solution.setZeroes(matrix1)

print("Output Matrix:")
for row in matrix1:
    print(row)

assert matrix1 == [[1,0,1],[0,0,0],[1,0,1]], f"Test Case 1 Failed: {matrix1}"


# Test Case 2
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print("\nTest Case 2:")
print("Input Matrix:")
for row in matrix2:
    print(row)

solution.setZeroes(matrix2)

print("Output Matrix:")
for row in matrix2:
    print(row)

assert matrix2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]], f"Test Case 2 Failed: {matrix2}"


# Test Case 3 (Single Row)
matrix3 = [[1, 0, 3]]
print("\nTest Case 3:")
print("Input Matrix:")
for row in matrix3:
    print(row)

solution.setZeroes(matrix3)

print("Output Matrix:")
for row in matrix3:
    print(row)

assert matrix3 == [[0, 0, 0]], f"Test Case 3 Failed: {matrix3}"


# Test Case 4 (Single Column)
matrix4 = [[1], [0], [3]]
print("\nTest Case 4:")
print("Input Matrix:")
for row in matrix4:
    print(row)

solution.setZeroes(matrix4)

print("Output Matrix:")
for row in matrix4:
    print(row)

assert matrix4 == [[0], [0], [0]], f"Test Case 4 Failed: {matrix4}"


# Test Case 5 (No Zeros)
matrix5 = [[1,2,3],[4,5,6],[7,8,9]]
print("\nTest Case 5:")
print("Input Matrix:")
for row in matrix5:
    print(row)

solution.setZeroes(matrix5)

print("Output Matrix:")
for row in matrix5:
    print(row)

assert matrix5 == [[1,2,3],[4,5,6],[7,8,9]], f"Test Case 5 Failed: {matrix5}"

print("\nAll test cases passed successfully!")

