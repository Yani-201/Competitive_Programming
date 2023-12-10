class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaced=""
        space=set(spaces)
        for i in range(len(s)):
            if i not in space:
                spaced+=s[i]
            else:
                spaced+=" "
                spaced+=s[i]
        return spaced
        