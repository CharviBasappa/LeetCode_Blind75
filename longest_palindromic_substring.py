class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest=""
        for i in range(len(s)):
            odd_palindrome = expandAroundCenter(i, i)
            even_palindrome = expandAroundCenter(i, i+1)

            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest
    
# Test Cases    
sol = Solution()
print(sol.longestPalindrome("babad"))  # Output: "bab" (or "aba")
print(sol.longestPalindrome("cbbd"))   # Output: "bb"
print(sol.longestPalindrome("a"))      # Output: "a"
print(sol.longestPalindrome("ac"))     # Output: "a" (or "c")