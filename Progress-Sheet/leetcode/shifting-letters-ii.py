class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*len(s)
        for q in shifts:
            if q[2] == 0:
                op=-1
            else:
                op=1
            prefix[q[0]]+=op
            if q[1] < len(s)-1:
                prefix[q[1]+1]-=op

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        ans =""
        for j in range(len(s)):
            temp = (((ord(s[j]) + prefix[j]) - ord('a')) % 26) + 97
            ans += chr(temp)
        return ans

        