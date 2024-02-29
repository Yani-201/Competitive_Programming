class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # visited = set()
        # left = 0
        # right = 0
        # ans = float('inf')
        # while right < len(cards):
        #     if cards[right]  not in visited:
        #         visited.add(cards[right])
        #         right +=1
        #     else:
        #         while cards[right] in visited:
        #             ans = min(ans, right-left +1)
        #             visited.remove(cards[left])
        #             left +=1
        # return ans if ans != float('inf') else -1

        #optional(not sliding windo solution)
        cardLocations = {}
        minLen = float('inf')
        for idx,card in enumerate(cards):
            if card in cardLocations:
                minLen = min(minLen,idx-cardLocations[card]+1)
            cardLocations[card]=idx
        return -1 if minLen == float('inf') else minLen
                
            