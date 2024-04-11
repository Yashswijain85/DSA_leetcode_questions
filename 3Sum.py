class Solution(object):
    def threeSum(self, nums):
        '''n = len(nums)
        lst = []
        x = nums[0]
        for i in range(n):
            for j in range(1,n):
                if x + nums[i] + nums[j] == 0:
                    lst.append([x, nums[i], nums[j]])
        return lst'''

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        triplets = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triplets
