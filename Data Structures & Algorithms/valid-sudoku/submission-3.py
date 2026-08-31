class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidChunk(chunk:List[str])->bool:
            for i in range(1, 10):
                if chunk.count(str(i)) > 1:
                    return False
            return True

        #construct cols
        cols = [[board[j][i] for j in range(9)] for i in range(9)]
        """
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            cols.append(col)
        """
        #construct squares
        squares = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = []
                for k in range(3):
                    for l in range(3):
                        square.append(board[i+k][j+l])
                squares.append(square)
        
        for row in board:
            if not isValidChunk(row):return False
        for col in cols:
            if not isValidChunk(col):return False
        for square in squares:
            if not isValidChunk(square):return False
        return True