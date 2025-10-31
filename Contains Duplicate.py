# Algo 1: 
# Time complexity : O(n)
# Space complexity : O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = {}
        
        for i in nums:
            if i not in nums_count:
                nums_count[i] = 1
            else:
                nums_count[i] += 1
        print(nums_count)
        for x,y in nums_count.items():
            if y > 1:
                return True
        else:
            return False

# Algo 2:
# Time complexity : O(n.logn)
# Space complexity : O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
