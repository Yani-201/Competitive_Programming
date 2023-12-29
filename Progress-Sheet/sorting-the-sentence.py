class Solution:
    def sortSentence(self, s: str) -> str:
       
        ques = s.split()
        temp = [0]*(len(ques))
        for word in ques:
          temp[int(word[-1])-1]=word[:-1]
       
        return " ".join(temp)