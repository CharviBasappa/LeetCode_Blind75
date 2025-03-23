from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result

sol = Solution()

# Test case 1
intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]
print(sol.insert(intervals1, newInterval1))  # Output: [[1,5],[6,9]]

# Test case 2
intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8]
print(sol.insert(intervals2, newInterval2))  # Output: [[1,2],[3,10],[12,16]]

# Test case 3 (no intervals)
intervals3 = []
newInterval3 = [5,7]
print(sol.insert(intervals3, newInterval3))  # Output: [[5,7]]

# Test case 4 (insert at beginning)
intervals4 = [[6,9]]
newInterval4 = [1,2]
print(sol.insert(intervals4, newInterval4))  # Output: [[1,2],[6,9]]
