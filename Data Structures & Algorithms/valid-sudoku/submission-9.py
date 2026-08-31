class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidChunk(chunk:List[str])->bool:
            """
            for i in range(1, 10):
                if chunk.count(str(i)) > 1:
                    return False
            """
            """
            seen = set()
            for x in chunk:
                if x in seen: return False
                if x!='.': seen.add(x)
            """
            return len(set(chunk)) + chunk.count('.') == 10 or len(set(chunk)) == 9
        cols = [[board[j][i] for j in range(9)] for i in range(9)]
        squares = [[board[i+k][j+l] for k in range(3) for l in range(3) ]for i in range(0,9,3) for j in range(0,9,3)]
        for row in board:
            if not isValidChunk(row):return False
        for col in cols:
            if not isValidChunk(col):return False
        for square in squares:
            if not isValidChunk(square):return False
        return True