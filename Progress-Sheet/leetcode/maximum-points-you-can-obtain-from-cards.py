class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        size = len(cardPoints) - k

        i, j = 0, size
        cur_sum = sum(cardPoints[i:j])

        maxi = total - cur_sum
        while j < len(cardPoints):
            cur_sum -= cardPoints[i]
            cur_sum += cardPoints[j]

            maxi = max(maxi, total-cur_sum)
            i += 1
            j += 1
        return maxi


        