class Solution(object):
    def isValidSudoku(self, board):
        for row in board: 
            filtered = [cell for cell in row if cell != "." ]
            if len(set(filtered)) < len(filtered): 
                return False 

        for col in range(9):
            column = [board[row][col] for row in range(9)]
            filtered = [cell for cell in column if cell != "." ]
            if len(set(filtered)) < len(filtered): 
                return False 
        
        for box_row in range(0, 9, 3):# gives 0, 3, 
            for box_col in range(0, 9, 3):   # gives 0, 3, 6
                box = [board[box_row + r][box_col + c] for r in range(3) for c in range(3)]
                filtered = [cell for cell in box if cell != "." ]
                if len(set(filtered)) < len(filtered): 
                    return False 
            

        return True 
        
        