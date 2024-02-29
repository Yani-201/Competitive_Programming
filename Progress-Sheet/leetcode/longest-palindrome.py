class Solution:
    def longestPalindrome(self, s: str) -> int:
        tracker = Counter(s)
        length = 0
        odds = False
        for letter in tracker:
            if tracker[letter] % 2 == 1:
                odds = True
            length += ((tracker[letter]) - (tracker[letter]%2))

        if odds:
            return length + 1
        else:
            return length        