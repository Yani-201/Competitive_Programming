class Solution:

    def __init__(self):
        self.i = 0

    def decodeString(self, s: str) -> str:
        result = ""
        while self.i < len(s) and s[self.i] != ']':
            if s[self.i].isdigit():
                k = ""
                while s[self.i].isdigit():
                    k += s[self.i]
                    self.i +=1
                k = int(k)
                self.i += 1
                r = self.decodeString(s)
                result += r * k
                self.i += 1
            else:
                result += s[self.i]
                self.i += 1
                
        return result


