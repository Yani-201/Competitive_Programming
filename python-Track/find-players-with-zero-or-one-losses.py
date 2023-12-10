class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss={}
        players=set()
        answer=[[],[]]

        for i in range(len(matches)):
            if matches[i][1] not in loss:
               loss[matches[i][1]]=1
            else:
                loss[matches[i][1]]+=1

            players.add(matches[i][0])
            players.add(matches[i][1])

        for i in players:
            if i not in loss:
                answer[0].append(i)
            elif loss[i]==1:
                answer[1].append(i)
        answer[0].sort()
        answer[1].sort()

        return answer


        

        