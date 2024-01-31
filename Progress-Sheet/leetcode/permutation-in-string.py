class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        
        s=defaultdict(int)
        check=defaultdict(int)

        if len(s1)>len(s2):
            return False

        for i in range(r):
            check[s2[i]]+=1
            s[s1[i]]+=1
        if s==check:
            return True

        
        while r < len(s2):
            check[s2[l]]-=1
            check[s2[r]]+=1
            
            if check[s2[l]]==0:
                del check[s2[l]]
            l+=1
            r+=1

            if s==check:
               return True
                
        return False
        