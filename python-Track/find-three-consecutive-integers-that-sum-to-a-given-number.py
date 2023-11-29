class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num%3 != 0:
            return []
        else:
            i=num//3
            return [i-1, i, i+1]
        