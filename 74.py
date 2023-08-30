class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        t = 0
        b = len(matrix) - 1
        found = False
        while t <= b:
            row = (t+b)//2
            if matrix[row][-1] < target:
                t = row + 1
            elif matrix[row][0] > target:
                b = row - 1
            else:
                t = row
                found = True
                break

        if found == False:
            return False

        l = 0
        r = len(matrix[t]) - 1

        while l <= r:
            mid = (l + r)//2
            if matrix[t][mid] < target:
                l = mid + 1
            elif matrix[t][mid] > target:
                r = mid - 1
            else:
                return True

        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

s = Solution()
s.searchMatrix(matrix,3)
