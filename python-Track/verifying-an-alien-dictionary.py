class Solution:
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lex=defaultdict(int)
        for i in range(len(order)):
            lex[order[i]]=i
        # print(lex)
        if len(words)==1: 
            return True
        for j in range(len(words)-1):
            i=0
            while i< min(len(words[j]), len(words[j+1])):
                if lex[words[j][i]]>lex[words[j+1][i]]:
                    return False
                elif lex[words[j][i]]==lex[words[j+1][i]]:
                    i+=1
                elif lex[words[j][i]]<lex[words[j+1][i]]:
                    break
            if i==min(len(words[j]), len(words[j+1])) and (len(words[j])>len(words[j+1])): 
                return False
        return True   
