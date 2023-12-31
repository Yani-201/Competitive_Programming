class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_of_evens = sum(x for x in nums if x % 2 == 0)
        ans = []

        for val, index in queries:
            if nums[index] % 2 == 0:
                sum_of_evens -= nums[index]

            nums[index] += val

            if nums[index] % 2 == 0:
                sum_of_evens += nums[index]

            ans.append(sum_of_evens)

        return ans

        