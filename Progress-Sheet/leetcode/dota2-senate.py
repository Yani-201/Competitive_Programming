class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        order = deque(senate)
        count = Counter(senate)
        banR, banD = 0, 0
        leftR, leftD = count['R'], count['D']
        while len(order) > 1:
            turn = order.popleft()
            if turn == 'R':
                if banR == 0:
                    banD += 1
                    order.append(turn)
                else:
                    banR -= 1
                    leftR -= 1
            else:
                if banD == 0:
                    banR += 1
                    order.append(turn)
                else:
                    banD -= 1
                    leftD -= 1
            if leftR == len(order):
                return 'Radiant'
            if leftD == len(order):
                return 'Dire'

        last = order.pop()
        return 'Radiant' if last == 'R' else 'Dire'
                
                
        