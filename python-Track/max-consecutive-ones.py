class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # l,r = 0,0
        # maxi=0
        # for r in range (len(nums)):
        #     if nums[l]==0:
        #         l+=1
        #     if nums[r]==0:
        #         dif= (r-l)
        #         maxi=max(maxi, dif)
        #         l=r
        #     elif r==len(nums)-1 and nums[r]==1:
        #         dif= (r-l)+1
        #         maxi=max(maxi, dif)
        maxi=0
        ct=0
        for i in nums:
            if i == 1:
                ct+=1
                continue
            
            maxi=max(maxi,ct)
            ct=0
        maxi = max(maxi, ct)    
        return maxi

        