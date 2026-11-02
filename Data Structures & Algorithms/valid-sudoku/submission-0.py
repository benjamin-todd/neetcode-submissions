class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [0] * 9
            for j in range(9):
                if board[i][j] == ".":
                    continue
                row[int(board[i][j]) - 1] += 1
                if row[int(board[i][j]) - 1] > 1:
                    return False
        
        for i in range(9):
            col = [0] * 9
            for j in range(9):
                if board[j][i] == ".":
                    continue
                col[int(board[j][i]) - 1] += 1
                if col[int(board[j][i]) - 1] > 1:
                    return False
        
        for box_r in range(0,9,3):
            for box_c in range(0,9,3):
                count = [0] * 9
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        if board[r][c] == ".":
                            continue
                        count[int(board[r][c]) - 1] += 1
                        if count[int(board[r][c]) - 1] > 1:
                            return False
        
        return True