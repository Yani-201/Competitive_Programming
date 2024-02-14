class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        acc = 0
        prefix=[0]*len(nums)
        ct=0
        track=defaultdict(int)
        for i in range(len(nums)):
            acc+=nums[i]
            prefix[i]=acc
            x=acc%k
            if x == 0:
                ct+=1
            if x in track:
                ct+=track[x]
            track[x]+=1

        return ct

            
                