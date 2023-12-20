class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]

        max_score=0
        max_list=[]

        for j in range(len(nums)+1):
            if j==0:
                numsL=0
            else:
                numsL= (j - nums[j-1]) 

            if j==len(nums):
                numsR=0
            elif j==0:
                numsR=nums[-1]
            else:
                numsR=(nums[-1] - nums[j-1])
            
            score=numsL+numsR

            if score>max_score:
                max_score=score
                max_list=[j]
            elif score==max_score:
                max_list.append(j)
            


        return max_list
        