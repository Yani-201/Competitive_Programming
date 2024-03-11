class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        num = ord(target)
        i = 0
        while i < len(letters):
            if ord(letters[i]) > num:
                return letters[i]
            i += 1
        return letters[0]
        