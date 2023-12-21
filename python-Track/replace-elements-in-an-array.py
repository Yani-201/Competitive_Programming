class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexed={}
        for k in range(len(nums)):
            indexed[nums[k]]=k

        for i in range(len(operations)):
            
            j=indexed[operations[i][0]]
            del(indexed[operations[i][0]])
            nums[j]=operations[i][1]
            indexed[operations[i][1]]=j
            
        return nums
        