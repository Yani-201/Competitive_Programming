class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i,j=0,k-1
        mini,cur=0,0
        for x in blocks[i:j+1]:
            if x=='W':
                cur+=1

        
        mini=cur

        if len(blocks)==1:
            return mini
        while j<len(blocks):
            j+=1
            if j==len(blocks):
                break 
            if blocks[j]=='W':
                cur+=1
            if blocks[i]=='W':
                cur-=1
            i+=1

            mini=min(cur,mini)

        return mini


        