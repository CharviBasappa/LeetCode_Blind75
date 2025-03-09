import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return cleaned_s == cleaned_s[::-1]

# Sample Test Cases
solution = Solution()

s1 = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s1))  # Output: True

s2 = "race a car"
print(solution.isPalindrome(s2))  # Output: False

s3 = " "
print(solution.isPalindrome(s3))  # Output: True

s4 = "No 'x' in Nixon"
print(solution.isPalindrome(s4))  # Output: True

s5 = "12321"
print(solution.isPalindrome(s5))  # Output: True

s6 = "Hello, World!"
print(solution.isPalindrome(s6))  # Output: False
