class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi = 0
        basket1 = [-1, 0]
        basket2 = [-1, 0]

        i, j = 0, 0
        while j < len(fruits):
            if basket1[0] == -1 or basket1[0] == fruits[j]:
                basket1[0] = fruits[j]
                basket1[1] += 1
                j += 1
            elif basket2[0] == -1 or basket2[0] == fruits[j]:
                basket2[0] = fruits[j]
                basket2[1] +=1
                j += 1
            else:
                if fruits[i] == basket1[0]:
                    basket1[1] -=1
                    if basket1[1] == 0:
                        basket1[0] = -1
                elif fruits[i] == basket2[0]:
                    basket2[1] -= 1
                    if basket2[1] == 0:
                        basket2[0] = -1
                i+=1

            maxi = max(maxi, j-i)

        return maxi

        