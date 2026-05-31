# Using extra space
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums)-1
        result = [0] * (len(nums))
        for i in range(len(nums)):
            if(nums[i] % 2 == 0):
                result[start] = nums[i]
                start+=1
            else:
                result[end] = nums[i]
                end -= 1
        return result

# Time complexity -> O(n)
# Space complexity -> O(n)

## Optimized approach : using Two Pointers
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[even], nums[i] = nums[i], nums[even]
                even += 1
        return nums

# Time complexity -> O(n)
# Space complexity -> O(1)

# Two pointer approach
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1

        while i<j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 == 0:
                i += 1

            if nums[j] % 2 == 1:
                j -= 1

        return nums

# Time complexity -> O(n)
# Space complexity -> O(1)
