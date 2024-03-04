class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def findsymbol(n,k):
            if n == 1:
                return 0
            parent = findsymbol(n-1, math.ceil(k/2))
            if k % 2 == 0:
                return 1 if parent == 0 else 0
            else:
                return 0 if parent == 0 else 1
        return findsymbol(n,k)
            
        
