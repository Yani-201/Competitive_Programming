class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified=0
        for i in range(1, len(nums)):
            if modified>1:break
            if nums[i]<nums[i-1]:
                if i==1:
                    nums[i-1]=nums[i]
                else: 
                    if nums[i]<nums[i-2]:
                        nums[i]=nums[i-1]
                    else:
                        nums[i-1]=nums[i-2]
                modified+=1
           

            else:continue

        if modified<=1:
            return True
        else:
            return False