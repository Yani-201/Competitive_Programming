class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        maxi=0
        cur=1
        for i in range(len(nums)-1):
            if nums[i+1]==(nums[i]+1):
                cur+=1
            elif nums[i+1]==(nums[i]):
                cur+=0
            else:
                maxi=max(maxi,cur)
                cur=1

        return max(maxi,cur)

        