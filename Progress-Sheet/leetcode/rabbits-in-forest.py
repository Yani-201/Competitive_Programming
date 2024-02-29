# from collections import Counter
# from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = Counter(answers)
        total = 0
        for rabbit in rabbits:
            if rabbit == 0:
                total += rabbits[rabbit]
            else:
                total += (rabbit + 1) * ((rabbits[rabbit] + rabbit) // (rabbit + 1))
        return total
