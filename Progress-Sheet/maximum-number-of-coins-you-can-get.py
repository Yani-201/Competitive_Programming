class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mine=0
        i=0
        j=len(piles)-1
        while j>i:
            mine+=piles[j-1]
            i+=1
            j-=2
        return mine