class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping=defaultdict(str)
        for i in range(97,123):
            if i<106:
                mapping[str(i-96)]=chr(i)
            else:
                mapping[str(i-96)+"#"]=chr(i)
        # print(mapping)
        
        ans=""
        i=0
        while i<len(s):
            if (s[i]=="1" or s[i]=="2") and (i+2)<len(s) and s[i+2]=="#":
                ans+=mapping[s[i:i+3]]
                i+=3
                continue

            ans+=mapping[s[i]]
            i+=1
        return ans
        