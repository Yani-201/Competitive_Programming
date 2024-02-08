class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i,j=0,0
        x,y=0,0
        maxF, maxT=0, 0
        kF, kT = k,k
        while j<len(answerKey):
            if answerKey[j]=='F':
                if kT>0:
                    kT-=1
                    j+=1
                else:
                    maxT=max(maxT, j-i)
                    if answerKey[i]=='F':
                        kT+=1
                    i+=1          
            else:
                j+=1
        maxT=max(maxT, j-i)
        while y<len(answerKey):
            if answerKey[y]=='T':
                if kF>0:
                    kF-=1
                    y+=1
                else:
                    maxF=max(maxF, y-x)
                    if answerKey[x]=='T':
                        kF+=1
                    x+=1          
            else:
                y+=1
        maxF=max(maxF, y-x)
        
        return max(maxT, maxF)
        