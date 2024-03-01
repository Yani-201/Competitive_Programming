class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(path, closed, opened):
            if closed > opened:
                return 
            if len(path) == 2*n:
                ans.append("".join(path))
            if opened < n:
                path.append("(")
                backtrack(path, closed, opened+1)
                path.pop()
            if closed > n:
                return

            path.append(")")
            backtrack(path, closed+1, opened)
            path.pop()

        backtrack([], 0, 0)
        return ans

            
        