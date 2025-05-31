class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
      # Approach 1 
      lookup = {}
        for i,num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i
        return []
    # Approach 2
    n = len(nums)
       for i in range(n):
        for j in range(i+1,n):
            result = nums[i] + nums[j]
            if result == target:
                return [i,j]

# Time complexity --> O(n) -- for first Approach 
# Time complexity --> O(n^2) -- for second approach 
