class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accum=0
        prefix_sum=[0]*len(nums)
        for i in range(len(nums)):
            accum+=nums[i]
            prefix_sum[i]=accum
        return prefix_sum
            