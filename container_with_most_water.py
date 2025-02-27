from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            max_water = max(max_water, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
    
#Sample Test Cases
sol = Solution()

height1 = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height1))  # Output: 49

height2 = [1,1]
print(sol.maxArea(height2))  # Output: 1

height3 = [4,3,2,1,4]
print(sol.maxArea(height3))  # Output: 16

height4 = [1,2,1]
print(sol.maxArea(height4))  # Output: 2

