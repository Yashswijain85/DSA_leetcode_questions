# Approach 1 
Time complexity -> O(n)
Space complexity -> O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = -1 
        one = -1
        two = -1
        for num in nums:
            if num == 0:
                two += 1
                one += 1
                zero += 1 
                nums[two] = 2
                nums[one] = 1
                nums[zero] = 0
            if num == 1:
                two += 1
                one += 1
                # zero is sorted, so don't take it 
                nums[two] = 2
                nums[one] = 1
            if num == 2:
                two += 1
                nums[two] = 2

# Approach 2 
Time complexity -> O(n) + O(n) = O(n)
Space complexity -> O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for el in nums:
            count[el] += 1

        c = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[c] = i
                c += 1
