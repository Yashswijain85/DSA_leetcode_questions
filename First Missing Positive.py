# Time complexity --> O(n) 
# Space complexity --> O(n) 

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num >= 1]

        # If no positive numbers, 1 is the smallest missing positive
        if not nums:
            return 1

        smallest = min(nums)
        largest = max(nums)
        smallestpositiveint = 1

        # If smallest positive number is greater than 1
        if smallest > 1:
            return smallestpositiveint

        # Make a set for faster lookup
        num_set = set(nums)

        # Check from 1 to largest+1
        for i in range(1, largest + 2):
            if i not in num_set:
                return i
