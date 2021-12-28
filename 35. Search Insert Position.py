# -*- coding: utf-8 -*-
"""
Problem:
    Given a sorted array of distinct integers and a tafget value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.
Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
"""
# Standard Packages
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right, ans = 0, len(nums) - 1, len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)


nums = [1, 3, 5, 6]
target = 2
ans = Solution().searchInsert(nums, target)
print(ans)
