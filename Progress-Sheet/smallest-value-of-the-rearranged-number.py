class Solution:
    def smallestNumber(self, num: int) -> int:
        
        numstr=str(abs(num))
        if len(numstr)==1:
            return num
            
        temp=[]
        for i in numstr:
            temp.append(i)

        if num == abs(num):
            temp.sort()

            j=0
            while int(temp[j])==0:
                j+=1
            temp[0], temp[j] = temp[j], temp[0]

            ans= "".join(temp)
            return int(ans)

        else:
            temp.sort(reverse=True)
            ans= "".join(temp)
            return int(ans)*(-1)



        
 
        