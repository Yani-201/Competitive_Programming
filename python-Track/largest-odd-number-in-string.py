class Solution:
    def largestOddNumber(self, num: str) -> str: 
        ans=""
        
        if int(num[-1])%2 != 0:
          ans+=num
        
        else:
          for i in range(len(num) - 1, -1, -1):
            if int(num[i])%2 != 0:
              ans+=num[:i+1]
              break

        return ans
        