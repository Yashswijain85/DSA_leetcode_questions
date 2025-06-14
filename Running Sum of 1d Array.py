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

# Approach 3 --> in-place -- same complexity as above 
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        return nums

