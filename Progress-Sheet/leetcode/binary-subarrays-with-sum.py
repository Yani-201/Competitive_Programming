class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        acc=0
        prefix=[0]*len(nums)
        track=defaultdict(int)
        ct=0
        for i in range(len(nums)):
            acc+=nums[i]
            prefix=acc
            if acc==goal:
                ct+=1
            if acc-goal in track:
                ct+=track[acc-goal]

            track[acc]+=1

        return ct