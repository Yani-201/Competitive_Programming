class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # sort it in decreasing because i want the recent element to be the last to be seen
        deck.sort(reverse=True)
        que = deque([deck[0]])

        for i in range(1, len(deck)):
            last_see = que.pop()
            first_see = deck[i]
            # i want it to be in such a way that first_see is at top and last_see is at second so that it is appended back to the last according to the algorithm
            que.appendleft(last_see)
            que.appendleft(first_see)
        return que

        