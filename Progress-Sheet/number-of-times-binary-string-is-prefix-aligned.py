class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxi=0
        # summ=0 .... approach 2
        ones=0
        ct=0
        for i in range(len(flips)):
            
            maxi=max(maxi, flips[i])
            ones+=1
            if ones==maxi:
                ct+=1


            # summ+=flips[i] .... approach 2
            # sumi=(maxi*(maxi+1))/2 .... approach 2
            # if sumi=summ:  .... approach 2
            #   ct+=1
       

            # if maxi <= i+1: ... simpler approach
            #     ct+=1        ... simpler approach
        return ct



        