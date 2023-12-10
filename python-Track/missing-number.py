class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_sum=0
        list_sum=0
        for i in range(len(nums)):
            list_sum+=nums[i]
            all_sum+=(i+1)   
        return all_sum-list_sum     