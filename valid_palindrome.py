class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = []
        for char in s:
            if char.isalnum():
                palindrome.append(char.lower())

        return "".join(palindrome) == "".join(palindrome[::-1])
        # if("".join(palindrome) == "".join(palindrome[::-1])):
        #     return True
        # else:
        #     return False
    
# Time complexity -- O(n)
# Space complexity -- O(n) 
        
