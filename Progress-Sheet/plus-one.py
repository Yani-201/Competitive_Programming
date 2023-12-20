class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i=-1
        while abs(i)<=len(digits) and digits[i]==9:
            digits[i]=0
            i-=1
            
        if abs(i)>len(digits):
            digits[i+1]=1
            digits.append(0)
            
        else:
            digits[i]+=1
     

        return digits
        