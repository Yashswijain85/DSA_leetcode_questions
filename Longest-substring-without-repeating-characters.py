class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            char_set = set()
            left = 0
            max_length = 0

            for right in range(len(s)):
                while s[right] in char_set:
                    #found the duplicate
                    char_set.remove(s[left])
                    #so,shrink the window
                    left += 1
                # else expand the window
                char_set.add(s[right])
            
                #update the max length
                max_length = max(max_length,right-left+1)
            return max_length

# Time complexity -- O(n) -- because although we there is nested while loop, each character is processed at most twice, to add and remove from the set.
# Space complexity -- O(min(n,char_set)
