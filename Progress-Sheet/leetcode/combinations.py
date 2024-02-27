class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []

        def backtrack(first_num, path):
            if len(path) == k:
                comb.append(path[:])
                return

            # check if there are enough numbers left for path length to be k
            if (k - len(path)) > (n - first_num + 1):
                return

            # first kind of implementation
            for num in range(first_num, n+1):
                path.append(num)
                backtrack(num+1, path)
                path.pop()

            # alternative part of implementation
            # if first_num > n:
            #     return
            #             # add nums and call backtrack 
            # path.append(first_num)
            # backtrack(first_num+1, path)
            #             # call backtrac without adding num 
            # path.pop()
            # backtrack(first_num+1, path)


        backtrack(1, [])
        return comb