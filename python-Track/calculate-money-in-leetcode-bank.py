class Solution:
    def totalMoney(self, n: int) -> int:
        num_of_weeks=n//7
        money=(num_of_weeks*28)
        # money+= (num_of_weeks*28) + (num_of_weeks-1)*(num_of_weeks)/2
        extra_days=n%7
        # money+= (extra_days * (num_of_weeks+1)) + ((extra_days-1)*(extra_days))/2
        for i in range(num_of_weeks):
            money+= i * 7
        for i in range(extra_days):
            money += (num_of_weeks + 1 + i) 

        return int(money)
        

        