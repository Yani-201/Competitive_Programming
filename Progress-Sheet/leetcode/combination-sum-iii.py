class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        candidates = [i for i in range(1,10)]
        ans=[]
        def backtrack(path, total, i):
            if total >= n or len(path) >= k:
                if total == n and len(path) == k:
                    ans.append(path[:])
                return

            for j in range(i, len(candidates)):
                path.append(candidates[j])
                total += candidates[j]
                backtrack(path, total, j+1)
                path.pop()
                total -= candidates[j]

        backtrack([], 0, 0)
        return ans
        