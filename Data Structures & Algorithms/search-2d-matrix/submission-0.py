class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1
        n = len(matrix[0])
        
        while left<=right:
            mid = (left + right)//2
            a = mid // n
            b = mid % n

            if matrix[a][b] > target:
                right = mid - 1
            elif matrix[a][b] < target:
                left = mid + 1
            elif matrix[a][b] == target:
                return True
        return False
        