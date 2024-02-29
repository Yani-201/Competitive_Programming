class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ops = 0
        while target > 1:
                
            if target % 2 == 1:
                ops += 1
                target -= 1
            else:
                if maxDoubles > 0:
                    ops += 1
                    target -= (target//2)
                    maxDoubles -= 1 
                else:
                    ops += (target-1)
                    break

        return ops
        