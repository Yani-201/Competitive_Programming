class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = []
        for i in s:
            if i.isalnum():
                sen.append(i.lower())
        words="".join(sen)

        j = 0
        k = len(words)-1
        while k > j:
            if words[k] != words[j]:
                return False
            else:
                j += 1
                k -= 1
        return True        