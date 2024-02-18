class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        ans = []
        while first < len(firstList) and second < len(secondList) :
            start = max(firstList[first][0], secondList[second][0])
            end = min(firstList[first][1], secondList[second][1])

            if end >= start:
                ans.append([start,end])
            
            if firstList[first][1] > secondList[second][1] :
                second+=1
            else:
                first+=1

        return ans

            
