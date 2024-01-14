class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        read = 0

        ans=0

        while read < len(nums):
            
            if nums[read] != val:
                nums[read], nums[write] = nums[write], nums[read]
                write = write + 1
                ans+=1

            read = read + 1
        return ans
        