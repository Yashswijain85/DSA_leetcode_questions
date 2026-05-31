# Approach 1 : using Extra space
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        even, odd = 0, 1
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                result[even] = nums[i]
                even += 2
            if nums[i] % 2 != 0:
                result[odd] = nums[i]
                odd += 2
        return result
# Time complexity  : O(n)
# Space complexity : O(n)

# Approach 2 : Using two pointer approach
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1

        while i< len(nums) and j < len(nums):
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 == 0:
                i += 2
            
            if nums[j] % 2 != 0:
                j += 2
        return nums

# Time complexity  : O(n)
# Space complexity : O(1)


