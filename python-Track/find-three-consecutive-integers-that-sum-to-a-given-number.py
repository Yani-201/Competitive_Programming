class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n=[]
        if num%3 != 0:
            return n
        else:
            i=num//3
            n.append(i-1)
            n.append(i)
            n.append(i+1)
            return n
        