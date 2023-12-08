class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        common = set(list1) & set(list2)
        index_sum={}
        answer=[]
        
        for word in common:
            j= list1.index(word)
            i= list2.index(word)
            index_sum[word]=i+j
        minimum = min(index_sum.values())
        
        for k in index_sum:
            if index_sum[k]==minimum:
                answer.append(k)
        
        return answer
        