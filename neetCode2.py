# Arlen Griswold
# May 8th, 2026
# Lab 11 - NeetCode: Valid Anagram
# https://neetcode.io/problems/is-anagram

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
