class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur=sum(nums[0:k])
        maxi=cur
        i,j=1,k

        while j<len(nums):
            cur+=nums[j]
            cur-=nums[i-1]
            maxi=max(cur,maxi)
            i+=1
            j+=1
        return maxi/k


        