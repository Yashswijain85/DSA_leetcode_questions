class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0  # Position to place the next non-zero element

        # First pass: move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Second pass: fill the remaining positions with zeroes
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
# Time complexity : O(n)
# Space complexity : O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0 

        for i in range(len(nums)): 
            if nums[i] != 0:
                nums[insert_pos],nums[i] = nums[i],nums[insert_pos]
                insert_pos += 1

# Time complexity -- O(n)
# Space complexity -- O(1)
