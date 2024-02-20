class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)//2):
        #     s[i], s[0-(i+1)] = s[0-(i+1)], s[i]
        def recursive(i,j):
            if i >= j:
                return
            s[i], s[j] = s[j], s[i]
            return recursive(i+1, j-1)
            
        recursive(0, len(s)-1)
        