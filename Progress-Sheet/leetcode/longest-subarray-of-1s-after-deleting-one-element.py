class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not 0 in nums:
            return len(nums) - 1
        if not 1 in nums:
            return 0
        i,j=0,0
        flag=False
        length=0
        while j<len(nums):
            if nums[j]==0:
                if flag:
                    length=max(length,j-i-1)
                    if nums[i]==0:
                        flag=False
                    i+=1
                else: 
                    flag=True
                    j+=1
            else:
                j+=1
        length=max(length,j-i-1)
        return length