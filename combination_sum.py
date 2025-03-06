from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                result.append(list(current_combination))
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_combination, current_sum + candidates[i])
                current_combination.pop()
        
        backtrack(0, [], 0)
        return result


# Sample Test Cases
solution = Solution()

candidates = [2, 3, 6, 7]
target = 7
print(solution.combinationSum(candidates, target))  #Output: [[2, 2, 3], [7]]

candidates = [2, 3, 5]
target = 8
print(solution.combinationSum(candidates, target))  #Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates = [2]
target = 1
print(solution.combinationSum(candidates, target))  #Output: []
