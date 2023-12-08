class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        Rearranged=[]
                
        for i in range(len(nums)):
            if abs(nums[i]) == nums[i]:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums)//2):
            Rearranged.append(positive[i])
            Rearranged.append(negative[i])

        return Rearranged