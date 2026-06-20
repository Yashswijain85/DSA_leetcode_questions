## Brute-Force approach:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
# Time Complexity :  O(m*n)
# Space Complexity : O(1)

## Better approach:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.binarySearch(matrix[i], target):
                return True
        return False


    def binarySearch(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# Time Complexity :  O(n*log(m))
# Space Complexity : O(1)

## Optimal approach:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row, col = 0, m-1

        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1 # if target is bigger we cannot find it in a row
            else:
                col -= 1
        return False
# Time Complexity :  O(n+m)
# Space Complexity : O(1)
