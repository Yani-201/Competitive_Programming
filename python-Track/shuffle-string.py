class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled=""
        letter_order={}

        for i in range(len(indices)):
            letter_order[indices[i]]=s[i]
       
        for j in range(len(s)):
            shuffled+=letter_order[j]
            
        return shuffled