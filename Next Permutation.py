class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        index = -1

        # Find the breaking point
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i # found the breaking point
                break

        # If we don't find the breaking point -- then this is the last permutation
        # return the smallest or first permutation
        if index == -1:
            nums.reverse()
            return nums

        # Find the next greater digit than the breaking point from the end
        for i in range(n-1, -1, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Reverse the right part of breaking point of the array to get the smallest permutation
        left, right = index + 1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

# Time complexity -> O(n)
# Space complexity -> O(1)
