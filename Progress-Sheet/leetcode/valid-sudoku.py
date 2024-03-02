class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_row = defaultdict(set)
        sudoku_col = defaultdict(set)
        sudoku_box = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    num = board[row][col]
                    if (num in sudoku_row[row]) or (num in sudoku_col[col]) or (num in sudoku_box[(row//3, col//3,)]):
                        # print(num, row, col)
                        return False
                    sudoku_row[row].add(num)
                    sudoku_col[col].add(num)
                    sudoku_box[(row//3, col//3,)].add(num)

        return True
        