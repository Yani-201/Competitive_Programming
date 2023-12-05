class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left, right = 0,0
        max_sum=0
        sums=0
        good_int =  ""

        for right in range(len(num)):

            if num[left]!=num[right]:
                left=right

            if right-left == 2:
                sums=((int(num[left]))*3)
                if sums>=max_sum:
                    max_sum=sums
                    good_int = num[left:right+1]
  
        return good_int

