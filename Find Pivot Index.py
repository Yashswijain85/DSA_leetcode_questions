# Time complexity = O(n) + O(n) = O(n)
# Space complexity = O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum += num

        left_sum = 0 
        for i in range(0,len(nums)):
            if left_sum == total_sum - left_sum -nums[i]:
                return i
            else:
                left_sum += nums[i]
        else:
            return -1

