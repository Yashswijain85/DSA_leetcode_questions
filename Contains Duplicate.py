Time complexity : O(n)
Space complexity : O(n)
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
