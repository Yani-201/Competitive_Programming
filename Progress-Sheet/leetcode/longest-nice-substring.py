class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        letters = set(s)
        for idx, cxr in enumerate(s):
            if cxr.swapcase() not in letters:
                left = self.longestNiceSubstring(s[:idx])
                right = self.longestNiceSubstring(s[idx+1:])
                return right if len(right) > len(left) else left

        return s
        