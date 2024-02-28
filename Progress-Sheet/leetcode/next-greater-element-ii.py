class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono =  []
        ans = [-1]*len(nums)
        for i in range(len(nums)*2):
            idx = i % len(nums)
            while len(mono) > 0 and nums[idx] > mono[-1][1]:
                temp = mono.pop()
                if ans[temp[0]] == -1:
                    ans[temp[0]] = nums[idx]
            mono.append([idx, nums[idx]])
        return ans
        