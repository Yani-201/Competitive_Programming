class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track=defaultdict(int)
        prefix=[0]*len(nums)
        acc=0
        ct=0
        for i in range(len(nums)):
            acc+=nums[i]
            prefix[i]=acc
            if acc == k:
                ct +=1
            if acc - k in track:
                ct += track[acc-k] 
            track[prefix[i]]+=1
        return ct

        