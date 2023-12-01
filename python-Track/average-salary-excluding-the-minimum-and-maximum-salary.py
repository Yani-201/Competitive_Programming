class Solution:
    def average(self, salary: List[int]) -> float:
        #if sorting used i.e. nlogn time complexity
        salary.sort()
        sum = 0
        for i in range (1, len(salary)-1):
            sum+=salary[i]
        
        avg = sum/(len(salary)-2)
        return avg

        #if sorting not used just find the min/max value from array i.e. n time complexity
        # if salary[0]<salary[1]:
        #     #put max at index 0 , and min at index 1
        #     salary[0], salary[1] = salary[1], salary[0]
        # for i in range(2, len(salary)):
        #     if salary[i]>salary[0]:
        #         salary[0], salary[i] = salary[i], salary[0]
        #     elif salary[i]<salary[1]:
        #         salary[i], salary[1] = salary[1], salary[i]

        # sum = 0
        # for i in range (2, len(salary)):
        #     sum+=salary[i]
        
        # avg = sum/(len(salary)-2)
        # return avg