class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

##########     #########      ##########     #       #
#                  #          #        #     #       #
#                  #          #        #     #       #
#                  #          #        #     #       #
#                  #          #        #     #       #
##########         #          ##########     #########
         #         #          #        #         #
         #         #          #        #         #
         #         #          #        #         #
         #         #          #        #         #
##########         #          #        #         #


#########     #      #     #       #    ########     ########
    #         #      #     ##      #    #            #       #
    #         #      #     # #     #    #            #       #
    #         #      #     #  #    #    ########     #       #
    #         #      #     #   #   #    #            #       #
    #         #      #     #    #  #    #            #       #
    #         #      #     #     # #    #            #       #
    #         ########     #      ##    ########     ########
        def is_unit_valid(data):
            seen = set()
            for num in data:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
            return True
        # check for rows
        for row in board:
            if not is_unit_valid(row):
                return False
        

        # check for columns
        for col in range(9):
            prep_col = []
            for row in range(9):
                prep_col.append(board[row][col])
            if not is_unit_valid(prep_col):
                return False
        

        #check for squares
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                prep_square = []
                for i in range(3):
                    for j in range(3):
                        prep_square.append(board[row + i][col + j])
                if not is_unit_valid(prep_square):
                    return False
        return True