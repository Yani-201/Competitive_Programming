class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer=[]

        i=0
        while i < len(nums):
            answer.extend([nums[i+1]]*(nums[i]))
            i+=2
            
        return answer