class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(path, total, i):
            if total >= target:
                if total == target:
                    ans.append(path[:])
                return

            for j in range(i, len(candidates)):
                total += candidates[j]
                path.append(candidates[j])
                backtrack(path, total, j)
                total -= candidates[j]
                path.pop()

        backtrack([], 0, 0)
        return ans


        