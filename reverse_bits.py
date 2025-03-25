class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = (result << 1) | bit
        return result

# Sample test cases
sol = Solution()

# Example 1
n1 = 0b00000010100101000001111010011100
print(sol.reverseBits(n1))  # Output: 964176192

# Example 2
n2 = 0b11111111111111111111111111111101
print(sol.reverseBits(n2))  # Output: 3221225471
