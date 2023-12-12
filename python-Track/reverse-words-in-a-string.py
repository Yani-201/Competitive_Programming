class Solution:
    def reverseWords(self, s: str) -> str:
        
        split_reverse=s.split()
        split_reverse.reverse()
        
        joined=" ".join(split_reverse)

        return joined
        