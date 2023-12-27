class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """   """
        ans = []
        sort_nums = sorted(nums)
        for num in nums:
            ans.append(sort_nums.index(num))  #index returns the first occurence of the number so duplicate appearances of a number will not be a problem
        return ans