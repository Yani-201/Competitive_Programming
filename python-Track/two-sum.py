class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_trace={}
 
        for j,n in enumerate(nums):
            req=target-n
            if req not in num_trace:
                num_trace[n]=j
            else:
                return [j, num_trace[req]]



        