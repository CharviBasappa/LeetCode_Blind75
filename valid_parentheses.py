class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# 🔹 Function to Test Cases
def test():
    solution = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("{[()]}", True),
        ("{[(])}", False),
        ("[", False),
        ("]", False),
        ("", True),
    ]

    for s, expected in test_cases:
        result = solution.isValid(s)
        print(f"Input: {s} → Output: {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")

# Run test cases
test()
