class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        p_sum=0
        s_sum=0
        r1,c1, c2=0,0, len(mat)-1 

        while r1<len(mat) and c2<len(mat):
            p_sum+=mat[r1][c1]
            if c1!=c2:
                s_sum+=mat[r1][c2]
            r1+=1
            c1+=1
            c2-=1

        return s_sum+p_sum
            