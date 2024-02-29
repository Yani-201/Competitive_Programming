class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # self.maxi = 0
        # letters = set(s)

        # def max_letter_comb(letter, k):
        #     i, j, length = 0, 0, 0
        #     while j < len(s):
        #         if s[j] != letter:
        #             if k > 0:
        #                 k -= 1
        #                 j += 1
        #             else:
        #                 self.maxi = max(self.maxi, j-i)
        #                 if s[i] != letter:
        #                     k += 1
        #                     i += 1
        #                 else:
        #                     i += 1        
        #         else:
        #             j += 1
        #     self.maxi = max(self.maxi, j-i)

        # for cxr in letters: max_letter_comb(cxr, k)

        # return self.maxi


        # //// optional implementation
        count = {}
        max_f = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])

            if r-l+1 - max_f > k:
                count[s[l]] -= 1
                l += 1
        return r-l+1
        