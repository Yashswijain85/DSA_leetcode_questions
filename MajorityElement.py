class Solution(object):
    def majorityElement(self, nums):
        count = {}
        result, maxCount = 0, 0 

        for n in nums: 
            count[n] = 1 + count.get(n, 0) # if the given element in nums is present, that element 'n' will be added their, else, we have to add 0 --> this is the functioning of .get() in python
            
            # update result 
            result = n if count[n] > maxCount else result 

            ## Now update maxCount
            maxCount = max(count[n], maxCount)

        return result 
