class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        whole=len(set(nums))
        ct=0
        track = defaultdict(int)
        left=0

        for right in range(len(nums)):
            track[nums[right]]+=1

            while len(track)==whole:
                ct+=(len(nums)-right)

                track[nums[left]]-=1
                if track[nums[left]]==0:
                    del track[nums[left]]
                    
                left+=1

        return ct
