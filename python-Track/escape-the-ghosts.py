class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        min_ghost_move=float('inf')
        for i in ghosts:
            current_ghost_move = abs(i[0] - target[0]) + abs(i[1] - target[1])
            min_ghost_move = min(current_ghost_move, min_ghost_move)

        player_move=abs(target[0])+abs(target[1])
            
        return player_move<min_ghost_move