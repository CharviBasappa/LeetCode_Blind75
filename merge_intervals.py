from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged

# Sample test cases
if __name__ == "__main__":
    sol = Solution()

    test1 = [[1,3],[2,6],[8,10],[15,18]]
    print("Input:", test1)
    print("Merged:", sol.merge(test1))  # Expected: [[1,6],[8,10],[15,18]]

    test2 = [[1,4],[4,5]]
    print("Input:", test2)
    print("Merged:", sol.merge(test2))  # Expected: [[1,5]]

    test3 = [[1,4],[0,2],[3,5]]
    print("Input:", test3)
    print("Merged:", sol.merge(test3))  # Expected: [[0,5]]

    test4 = [[1,4],[5,6]]
    print("Input:", test4)
    print("Merged:", sol.merge(test4))  # Expected: [[1,4],[5,6]]
