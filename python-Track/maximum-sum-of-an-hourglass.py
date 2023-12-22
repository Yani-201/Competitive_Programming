class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        maxi = 0
        r=0
        while r<len(grid)-2:
            c=0
            while c<len(grid[0])-2:
                summ = sum(grid[r][c:c+3]) + grid[r+1][c+1] + sum(grid[r+2][c:c+3])
                maxi = max(summ, maxi)
                c+=1

            r+=1

        return maxi
        