class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxi = nums[0]
        cur_sum = nums[0]
        for i in range(1,len(nums)):
            cur_sum += nums[i]
            cur_max = math.ceil(cur_sum / (i+1))
            maxi = max(maxi, cur_max)
        return maxi
