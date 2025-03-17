class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1

        return len(intervals) - count


# Sample Test Cases
solution = Solution()

intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
result1 = solution.eraseOverlapIntervals(intervals1)
print(f"Test Case 1: {result1}")

intervals2 = [[1, 2], [1, 2], [1, 2]]
result2 = solution.eraseOverlapIntervals(intervals2)
print(f"Test Case 2: {result2}")

intervals3 = [[1, 2], [2, 3]]
result3 = solution.eraseOverlapIntervals(intervals3)
print(f"Test Case 3: {result3}")

intervals4 = [[1, 100], [11, 22], [1, 11], [2, 12]]
result4 = solution.eraseOverlapIntervals(intervals4)
print(f"Test Case 4: {result4}")

intervals5 = []
result5 = solution.eraseOverlapIntervals(intervals5)
print(f"Test Case 5: {result5}")

intervals6 = [[-52, -31],[-53,-51],[-25,12],[-42, -18],[-41, -12],[-53, -48],[-51, -49],[-35, -17],[-21, -13],[-47, -40],[-32, -26]]
result6 = solution.eraseOverlapIntervals(intervals6)
print(f"Test Case 6: {result6}")