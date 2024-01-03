class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        ct=0
        for k in guards:
            matrix[k[0]][k[1]] = "G"
        for j in walls:
            matrix[j[0]][j[1]] = "W"
        c=0
        for i in guards:
            c+=1
            up, down, right, left=True, True, True, True
            ru, rd= i[0]-1 , i[0]+1
            cl, cr= i[1]-1, i[1]+1
            # counter = 0
            while(up or down or right or left):
                # counter += 1
                # if counter > 1000:
                #     print(i)
                #     print(up,down,left,right)
                #     break
                if ru>=0 and up:
                    # print("inloop")
                    if matrix[ru][i[1]] in ("G", "W", "V", "HV", "VH"):
                        up=False 
                    elif matrix[ru][i[1]] == 0:
                        matrix[ru][i[1]] = "V"
                        ru-=1
                    elif matrix[ru][i[1]]=="H":
                        matrix[ru][i[1]] += "V"
                        ru-=1
                    
                else:
                    # print("inloop")
                    up=False

                if rd<m and down:
                    if matrix[rd][i[1]] in ("G", "W", "V", "HV", "VH"):
                        # print("in loop")
                        down=False 
                    elif matrix[rd][i[1]] == 0:
                        # print("in loop")

                        matrix[rd][i[1]] = "V"
                        rd+=1
                    elif matrix[rd][i[1]]=="H":
                        matrix[rd][i[1]] += "V"
                        rd+=1

                else:
                    down=False

                if cl>=0 and left:

                    if matrix[i[0]][cl] in ("G", "W", "H", "VH", "HV"):
                        print(matrix[i[0]][cl])
                        left=False 
                    elif matrix[i[0]][cl] == 0:
                        matrix[i[0]][cl] = "H"
                        cl-=1


                    elif matrix[i[0]][cl]=="V":
                        matrix[i[0]][cl] += "H"
                        cl-=1

                else:
                    left=False

                if cr<n:
                    if matrix[i[0]][cr] in ("G", "W", "H", "VH", "HV"):
                        right=False 
                    elif matrix[i[0]][cr] == 0:
                        matrix[i[0]][cr] = "H"
                        cr+=1
                    elif matrix[i[0]][cr]=="V":
                        matrix[i[0]][cr] += "H"
                        cr+=1
                    
                else:
                    right=False
# 
        for x in range(len(matrix)):
            for y in matrix[x]:
                if y==0:
                    ct+=1

        print(matrix)

        return ct
        # if matrix[0][0] in ("G", "W", "V"):
        #     print(True)
        # else:
        #     print(False)
        # return 0
       