class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i=0
        while i<len(nums)-2:
            if nums[i+1]+nums[i+2]>nums[i]:
                return nums[i]+nums[i+1]+nums[i+2]
            else:
                i+=1
        return 0

        