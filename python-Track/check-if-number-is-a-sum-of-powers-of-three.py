class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l=set()
        
        while n!=0:
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

        