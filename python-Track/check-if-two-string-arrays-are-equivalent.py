class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word11=""
        word22=""

        for word in word1: word11+=word
        for words in word2: word22+=words

        if word11==word22: return True
        else: return False
