class Solution:
    def printVertically(self, s: str) -> List[str]:
        list_of_words=s.split() 
        max_length = len(sorted(list_of_words, key=lambda x: len(x), reverse=True)[0])
        vertical_print=[]
        for i in range(max_length):
            new=""
            for word in list_of_words:
                if i<len(word): new+=word[i]
                else: new+=" "

            vertical_print.append(new.rstrip())
        return vertical_print
            