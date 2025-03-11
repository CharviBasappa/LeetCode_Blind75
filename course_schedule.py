from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0

        while queue:
            course = queue.popleft()
            count += 1
            
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses
    
solution = Solution()

# Test Case 1: Possible to finish all courses
numCourses1 = 2
prerequisites1 = [[1, 0]]
print(solution.canFinish(numCourses1, prerequisites1))  # Output: True

# Test Case 2: Cycle exists, impossible to finish
numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(solution.canFinish(numCourses2, prerequisites2))  # Output: False

# Test Case 3: No prerequisites, can finish all courses
numCourses3 = 3
prerequisites3 = []
print(solution.canFinish(numCourses3, prerequisites3))  # Output: True

# Test Case 4: Multiple dependencies, but no cycle
numCourses4 = 4
prerequisites4 = [[1, 0], [2, 1], [3, 2]]
print(solution.canFinish(numCourses4, prerequisites4))  # Output: True

# Test Case 5: Complex case with cycle
numCourses5 = 4
prerequisites5 = [[1, 0], [2, 1], [3, 2], [0, 3]]
print(solution.canFinish(numCourses5, prerequisites5))  # Output: False

