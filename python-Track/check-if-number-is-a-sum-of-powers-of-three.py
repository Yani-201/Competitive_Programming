class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l=set()
        
        while n!=0:
            # in python log function with a base 3 gives an error at 243 so the if/else check is a way to solve that
            if n==243:
                x=int(log(n,3))+1
            else:
                x=int(log(n,3))
            print(x)
            if x in l:
                return False
            n = n-(3**x)
            l.add(x)

        return True

        #another approach
        #while n>1:
           # value,remain= divmod(n,3)
            #if remain==2:
                #return False 
            #n= value
        #return True 

        