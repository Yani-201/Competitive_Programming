class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        # this is because the order in subsets doesnt matter and we dont want any dublicates
        nums.sort()

        def backtrack(current, path, cur_len):
            if len(path) == cur_len and path not in subsets:
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
        