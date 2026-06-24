class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rook_r, rook_c = r, c
                    
        attack = 0
        movement = [(-1,0), (1,0), (0,-1), (0,1)]
        for moveR, moveC in movement:
            r, c = rook_r + moveR, rook_c + moveC
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'B':
                    break
                if board[r][c] == 'p':
                    attack += 1
                    break
                r += moveR
                c += moveC
        return attack