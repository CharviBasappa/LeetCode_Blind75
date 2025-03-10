from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lis = []
        
        for num in nums:
            idx = bisect.bisect_left(lis, num)
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num
            
        return len(lis)

#Sample Test Cases
solution = Solution()

nums1 = [10,9,2,5,3,7,101,18]
print(solution.lengthOfLIS(nums1))  # Output: 4

nums2 = [0,1,0,3,2,3]
print(solution.lengthOfLIS(nums2))  # Output: 4

nums3 = [7,7,7,7,7,7,7]
print(solution.lengthOfLIS(nums3))  # Output: 1

nums4 = [1,3,6,7,9,4,10,5,6]
print(solution.lengthOfLIS(nums4))  # Output: 6
