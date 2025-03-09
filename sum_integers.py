class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to get last 32 bits (for handling negative numbers)
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b:
            carry = (a & b)  # Carry where both bits are 1
            a = (a ^ b) & MASK  # Sum without carry
            b = (carry << 1) & MASK  # Move carry to left
            
        # If a is negative, get 32-bit signed integer
        return a if a <= MAX_INT else ~(a ^ MASK)

# Sample Test Cases
solution = Solution()

# Example Cases
print(solution.getSum(1, 2))  # Output: 3
print(solution.getSum(2, 3))  # Output: 5

# Additional Cases
print(solution.getSum(-1, 1))  # Output: 0
print(solution.getSum(-2, -3))  # Output: -5
print(solution.getSum(15, 25))  # Output: 40
print(solution.getSum(1000, -1000))  # Output: 0
