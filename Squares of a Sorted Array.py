# Time complexity --> O(n) 
# Space complexity --> O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        write_pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[write_pos] = nums[left] ** 2
                left += 1
            else:
                result[write_pos] = nums[right] ** 2
                right -= 1
            write_pos -= 1

        return result

