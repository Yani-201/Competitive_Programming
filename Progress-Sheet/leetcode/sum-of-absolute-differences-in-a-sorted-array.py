class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        acc=0
        prefix=[0]*(len(nums)+1)
        for i in range(len(nums)):
            acc+=nums[i]
            prefix[i+1]=acc

        ans=[]
        for j in range(len(nums)):
            before=(nums[j]*j)-prefix[j]
            after= (prefix[-1]-prefix[j])-(nums[j]*(len(nums)-j))
        
            summ=before+after
            ans.append(summ)
        return ans


        