class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency=(len(nums)//3)+1
        freq={}
        majority=[]
        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for j in freq:
            if freq[j]>=frequency:
                majority.append(j)

        
        return majority

