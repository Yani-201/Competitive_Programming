class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in range(len(self.matrix)): 
            acc=0 
            for col in range(len(self.matrix[0])):
                acc+=self.matrix[row][col]
                self.matrix[row][col]=acc
        for col in range(len(self.matrix[0])): 
            acc=0 
            for row in range(len(self.matrix)):
                acc+=self.matrix[row][col]
                self.matrix[row][col]=acc
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2][col2]
        if col1-1 >=0:
            ans -= self.matrix[row2][col1-1]
        if row1-1 >=0:
            ans -= self.matrix[row1-1][col2]
        if row1-1 >=0 and col1-1 >=0:
            ans += self.matrix[row1-1][col1-1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)