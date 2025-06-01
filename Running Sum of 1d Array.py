class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        sum = 0 
        for num in nums:
            sum += num
            running_sum.append(sum)

        return running_sum

# Time complexity : O(n)
# Space complexity : O(n)
