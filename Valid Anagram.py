# Time complexity -> O(kxn) = O(n^2)
# Space complexity -> O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        else:
            return True
