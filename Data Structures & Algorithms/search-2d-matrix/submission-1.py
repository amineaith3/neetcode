class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        hopla = [0] * (rows * cols)
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                hopla[i * cols + j] = col
        print(hopla)
        l, r = 0, rows * cols - 1
        while l <= r:
            mid = (l + r) // 2
            print(hopla[mid])
            if hopla[mid] == target:
                return True
            elif hopla[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False