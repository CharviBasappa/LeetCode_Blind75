class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# Test Cases    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
print(sol.lengthOfLongestSubstring("bbbbb"))    # Output: 1 ("b")
print(sol.lengthOfLongestSubstring("pwwkew"))   # Output: 3 ("wke")
print(sol.lengthOfLongestSubstring(""))         # Output: 0 (empty string)
print(sol.lengthOfLongestSubstring("dvdf"))     # Output: 3 ("vdf")