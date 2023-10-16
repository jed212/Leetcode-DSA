class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        binary search the rows to find which row contains target
        binary search the row found to find target
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row = 0
        last_row = rows - 1
        
        while first_row <= last_row:
            row = (last_row + first_row)// 2
            if target > matrix[row][-1]:
                first_row = row + 1
            elif target < matrix[row][0]:
                last_row = row - 1
            else:
                break
        if not first_row <= last_row:
            return False
        
        row = (last_row + first_row)// 2
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right)//2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
        return False