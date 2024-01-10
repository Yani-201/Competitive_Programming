class Solution:
    #this is new
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(answer)<=j:
                    answer.append([matrix[i][j]])
                else:
                    answer[j].append(matrix[i][j])
        return answer


        