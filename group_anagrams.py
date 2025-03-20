from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)
        
        return list(anagrams.values())

# Sample test cases
solution = Solution()

# Test case 1
strs1 = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs1))
# Expected Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Test case 2
strs2 = [""]
print(solution.groupAnagrams(strs2))
# Expected Output: [[""]]

# Test case 3
strs3 = ["a"]
print(solution.groupAnagrams(strs3))
# Expected Output: [["a"]]

# Test case 4 (additional)
strs4 = ["abc", "bca", "cab", "xyz", "zyx", "yxz", "foo", "ofo"]
print(solution.groupAnagrams(strs4))
# Expected Output: [["abc", "bca", "cab"], ["xyz", "zyx", "yxz"], ["foo", "ofo"]]
