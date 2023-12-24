# from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        traverse = []

        for i in range(m + n - 1):
            if i % 2 == 0:  # even diagonals
                r, c = min(i, m - 1), max(0, i - m + 1)
                while r >= 0 and c < n:
                    traverse.append(mat[r][c])
                    r -= 1
                    c += 1
            else:  # odd diagonals
                r, c = max(0, i - n + 1), min(i, n - 1)
                while r < m and c >= 0:
                    traverse.append(mat[r][c])
                    r += 1
                    c -= 1

        return traverse
