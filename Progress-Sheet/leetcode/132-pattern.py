class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mono = []
        mini = float('inf')
        for i in range(len(nums)):
            while len(mono) > 0 and mono[-1][0] <= nums[i]:
                mono.pop()
            if len(mono) > 0 and nums[i] > mono[-1][1]:
                return True

            mono.append([nums[i], mini])
            mini = min(mini, nums[i])

        return False
        