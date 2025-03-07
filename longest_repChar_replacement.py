class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        char_count = {}
        max_length = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right],0) + 1
            max_freq = max(max_freq, char_count[s[right]])

            while(right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length
    
# Test cases
solution = Solution()

print(solution.characterReplacement("ABAB", 2))  # Output: 4

print(solution.characterReplacement("AABABBA", 1))  # Output: 4

print(solution.characterReplacement("A", 1))  # Output: 1

print(solution.characterReplacement("AAAA", 2))  # Output: 4

print(solution.characterReplacement("ABCDE", 5))  # Output: 5
