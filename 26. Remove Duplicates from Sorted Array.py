from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = set()
        ptr = 0
        for idx, val in enumerate(nums):
            if val in nums_set:
                continue
            nums_set.add(val)
            nums[ptr] = val
            ptr += 1
        return ptr


if __name__ == "__main__":
    print("[26] Remove Duplicates from Sorted Array")
    main = Solution()
    nums = [1, 1, 2]
    print(main.removeDuplicates(nums))
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(main.removeDuplicates(nums))
