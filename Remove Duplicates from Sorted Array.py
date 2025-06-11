# Time complexity : O(n) 
# Space complexity : O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0  # pointer for last unique element

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # place the new unique element

        return i + 1  # length of array with unique elements

