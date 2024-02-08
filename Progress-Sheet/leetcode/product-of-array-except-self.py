class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        
        accf=1
        accb=1

        prefixfront=[0]*len(nums)
        prefixback=[0]*len(nums)
        
        j=len(nums)-1
        for i in range(len(nums)):
            accf*=nums[i]
            prefixfront[i]=accf
            accb*=nums[j]
            prefixback[j]=accb
            j-=1

        ans[0]=prefixback[1]
        ans[-1]=prefixfront[-2]
        for x in range(1,len(nums)-1):
            ans[x]=prefixfront[x-1]*prefixback[x+1]

        return ans