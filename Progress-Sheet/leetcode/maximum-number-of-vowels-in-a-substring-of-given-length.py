class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i,j=0,k-1
        vowel=('a','e','i','o','u')
        maxi=0
        cur=0
        for k in s[i:j+1]:
            if k in vowel:
                cur+=1
        
        while j<len(s)-1:
            maxi=max(cur,maxi)
            if s[i] in vowel:
                cur-=1
            i+=1
            j+=1
            if s[j] in vowel:
                cur+=1
        maxi=max(cur, maxi)
        return maxi
            
        