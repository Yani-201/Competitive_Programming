class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        mini=float('inf')
        cursum=0
        for i in range(len(nums)):
            cursum+=nums[i]
            while cursum>=target:
                cursum-=nums[j]
                mini=min(mini, i-j+1)
                j+=1
                       
        # if cursum>=target:
        #     mini=min(mini, i-j)

        return 0 if mini==float('inf') else mini

        