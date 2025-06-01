# Approach 1
# Time complexity : O(n)
# Space complexity : O(n)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        sum = 0 
        for num in nums:
            sum += num
            running_sum.append(sum)

        return running_sum

# Approach 2 : 
# Time complexity : O(n)
# Space complexity : O(1) --> in-place

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0 
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum

        return nums

