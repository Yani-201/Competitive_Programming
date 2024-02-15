class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        opened = 0

        for cxr in s:
            if cxr == "(":
                opened += 1
            else:
                if opened > 0:
                    opened -= 1
                else:
                    count += 1

        return opened + count
        