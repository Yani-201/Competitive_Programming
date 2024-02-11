class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        acc=0
        prefix=[0]*len(nums)
        maxi=float('-inf')
        mini=0
        for i in range(len(nums)):
            acc+=nums[i]
            prefix=acc
            maxi=max(maxi, acc - mini )
            mini=min(mini,acc)

        return maxi

