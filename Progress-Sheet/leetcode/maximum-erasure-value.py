class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = set()
        max_val = 0
        cur_sum = 0
        i, j = 0, 0

        while j < len(nums):
            if nums[j] not in visited:
                cur_sum += nums[j]
                visited.add(nums[j])
                j += 1
            else:
                cur_sum -= nums[i]
                visited.remove(nums[i])
                i += 1

            max_val = max(max_val, cur_sum)


        max_val = max(max_val, cur_sum)
        return max_val
