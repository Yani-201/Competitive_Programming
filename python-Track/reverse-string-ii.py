class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        new=[]
        i=0
        while i<len(s):
            x=s[i:i+k]
            new.append(x[::-1])
            new.append(s[i+k:i+(2*k)])

            i+=(2*k)

        return ''.join(new)
        