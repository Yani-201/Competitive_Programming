class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        cur=None
        for i in range(len(nums)):
            if nums[i]!=cur:
                cur=nums[i]
                nums[k]=nums[i]
                k+=1
      
        return k
        
        