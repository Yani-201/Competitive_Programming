class Solution:
    
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        answer=[]
        for word in words:
            
            if word[0].lower() in row1: row=row1
            elif word[0].lower() in row2: row=row2
            elif word[0].lower() in row3: row=row3

            j=1
            while j<len(word):
                if word[j].lower() in row:
                    j+=1
                    continue
                else: break
            if j == len(word): answer.append(word)
        return answer