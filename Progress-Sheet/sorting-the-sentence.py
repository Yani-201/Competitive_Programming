class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split()
        ans =[0]*len(temp)
        for word in temp:
            ans[int(word[-1])-1]=word[:-1]
        return " ".join(ans)
        