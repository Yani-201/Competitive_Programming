class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []

        def backtrack(current, path, cur_len):
            if len(path) == cur_len:
                subsets.append(path[:])
                return

         # check if there are enough numbers left for path length to be cur_len
            if (cur_len - len(path)) > (len(nums) - current + 1):
                return

            if current >= len(nums):
                return 

            path.append(nums[current])
            backtrack(current+1, path, cur_len)
            path.pop()
            backtrack(current+1, path, cur_len)


        for i in range(len(nums)+1):
            backtrack(0, [], i)

        return subsets

        