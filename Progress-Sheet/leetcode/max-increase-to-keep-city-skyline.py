class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [0]*n
        col_max = [0]*n

        for row in range(n):
            for col in range(n):
                row_max[row] = max(row_max[row], grid[row][col])
                col_max[col] = max(col_max[col], grid[row][col])

        print(row_max, col_max)

        increase = 0
        for row in range(n):
            for col in range(n):
               increase += min(row_max[row], col_max[col]) - grid[row][col]
        return increase
        