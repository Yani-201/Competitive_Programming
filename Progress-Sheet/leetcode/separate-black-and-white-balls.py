class Solution:
    def minimumSteps(self, s: str) -> int:
        if len(s)==1: return 0
        read, write = 0, 0, 
        count=0

        while read<len(s):

            if s[read]!='1':
                count+=abs(read-write)
                write+=1

            read+=1

        return count

        
        