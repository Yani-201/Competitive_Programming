class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans=[]
        for i in range(len(matrix[0])):
            k=[]
            for j in range(len(matrix)-1, -1,-1):
                k.append(matrix[j][i])
                # print(k)
            ans.append(k)
        # print(ans) 
        for m in range(len(matrix)):
            matrix[m]=ans[m]
        