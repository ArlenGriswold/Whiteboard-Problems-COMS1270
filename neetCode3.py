# Arlen Griswold
# Lab 11 - NeetCode: Two Integer
# May 8th, 2026
# https://neetcode.io/problems/two-integer-sum/solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []



