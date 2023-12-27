class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
#...Bubble sort
        # for i in range(len(nums)):
        #     swaps=0
        #     for j in range(len(nums)-i-1):  
        #         if nums[j]>nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #             swaps+=1 

        #     if swaps==0:
        #         break 

#...counting sort
        freq=[0]*3
        done=[]

        for i in range(len(nums)):
            freq[nums[i]]+=1

        for j in range(len(freq)):
            if freq[j]!=0:
                done.extend([j]*freq[j])
 
        for k in range(len(nums)):
            nums[k]=done[k]