# Time complexity --> O(n*m)
# Space complexity --> O(n*m)
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for row in image: 
            reversed_and_inverted_row = [1-x for x in row[::-1]]
            result.append(reversed_and_inverted_row)
        return result 

        
