class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(path, total, i):
            if total >= target:
                if total == target:
                    ans.append(path[:])
                return 

            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                total += candidates[j]
                backtrack(path, total, j+1)
                path.pop()
                total -= candidates[j]

        backtrack([], 0, 0)
        return ans

        