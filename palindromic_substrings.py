class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_around_center(left: int, right: int) -> int:

            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total_palindromes = 0

        for i in range(len(s)):
            total_palindromes += expand_around_center(i, i)
            total_palindromes += expand_around_center(i, i + 1)

        return total_palindromes

# Sample Test Cases
solution = Solution()
print(solution.countSubstrings("abc"))  # Output: 3 (["a", "b", "c"])
print(solution.countSubstrings("aaa"))  # Output: 6 (["a", "a", "a", "aa", "aa", "aaa"])
print(solution.countSubstrings("racecar"))  # Output: 10 (["r", "a", "c", "e", "c", "a", "r", "cec", "aceca", "racecar"])
print(solution.countSubstrings("abba"))  # Output: 6 (["a", "b", "b", "a", "bb", "abba"])
