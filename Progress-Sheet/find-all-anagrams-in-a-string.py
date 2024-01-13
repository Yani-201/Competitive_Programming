class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ct=Counter(p)
        k=len(p)
        cur_ct=Counter(s[0:k])
        i=1
        anagram=[]
        if ct==cur_ct:
            anagram.append(0)

        for j in range(k,len(s)):
            cur_ct[s[j]]+=1
            cur_ct[s[i-1]]-=1
            if cur_ct[s[i-1]]==0:
                del cur_ct[s[i-1]]
            if ct==cur_ct:
                anagram.append(i)
            i+=1

        return anagram
