class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix=[0]*len(nums)
        for request in requests:
            prefix[request[0]]+=1
            if request[1]+1<len(nums):
                prefix[request[1]+1]-=1
        for i in range(1, len(prefix)):
            prefix[i]+=prefix[i-1]
        prefix.sort()
        nums.sort()
        res=0
        for j in range(len(nums)):
            res+=(prefix[j]*nums[j])
        return res%((10**9)+7)
        