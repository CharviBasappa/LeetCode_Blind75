from typing import List
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        queue = deque([0])
        visited = set()
        
        while queue:
            start = queue.popleft()
            if start in visited:
                continue
            visited.add(start)
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    if end == len(s):
                        return True
                    queue.append(end)
        
        return False

# Test Cases
solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))  # Output: True
print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
