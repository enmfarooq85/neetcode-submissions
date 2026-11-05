class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen_row = set()
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if val in seen_row:
                        return False
                    seen_row.add(val)

        for c in range(9):
            seen_col = set()
            for r in range(9):
                val = board[r][c]
                if val != ".":
                    if val in seen_col:
                        return False
                    seen_col.add(val)

        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen_box = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]
                        if val != ".":
                            if val in seen_box:
                                return False
                            seen_box.add(val)
        
        return True
