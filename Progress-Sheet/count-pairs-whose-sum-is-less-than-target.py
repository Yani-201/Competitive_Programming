class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        ct=0
        while j>i:
            if (nums[i]+nums[j])<target:
                ct+=(j-i)
                i+=1
            else:
                j-=1

        return ct
        