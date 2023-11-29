class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=[]
        while x!=0:
            value,rem = divmod(x,10)
            num.append(rem)
            x=value
        return num== num[::-1]   

        