class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        if nums[-1] - nums[0] == 0:
            return 0
        for j  in range(1, len(nums)-1):
            if nums[j-1] == nums[-1] - nums[j]:
                return j
        
        if nums[-2] == 0:
            return len(nums)-1
        return -1
            