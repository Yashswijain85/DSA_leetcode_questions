# Time complexity --> O(n)
# Space complexity --> O(1)

# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            # If the char is not alpha-numeric, we will skip it
            # move the left pointer to the next alphanumeric character
            while left<right and not s[left].isalnum():
                left += 1
            #move the right pointer to the next alphanumeric character 
            while left<right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            # Move to inner side
            left += 1
            right -= 1
        return True
    
