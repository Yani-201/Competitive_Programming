class Solution:
    def maxScore(self, s: str) -> int:
        prefix_0=[]
        suffix_1=[0]*len(s)

        acc_0=0
        acc_1=0
        score=0

        j=len(s)-1

        for i in range(len(s)):
            if s[i]=='0':
                acc_0+=1
            prefix_0.append(acc_0)
            suffix_1[j]=acc_1

            if s[j]=='1':
                acc_1+=1
            j-=1

        for k in range(len(s)-1):
            cur_score=prefix_0[k]+suffix_1[k]
            score=max(score, cur_score)

        return score
    