class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ct5 = 0
        ct10 = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                ct5 += 1

            elif bills[i] == 10:
                if ct5 == 0:
                    return False
                ct10 += 1
                ct5 -= 1

            else:
                if ct10 == 0 and ct5 >= 3:
                    ct5 -= 3
                elif ct10 > 0 and ct5 > 0:
                    ct10 -= 1
                    ct5 -= 1
                else:
                    return False

        return True
        