class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #each row must contain 1-9 without repition 
        #each column must contain 1-9 w/o repition
        #each subgrid contains 1-9 w/o repition


        #hashmaps dont allow duplicate keys 


        #create a dfault set within the dictionary 
        #hashmap for each col/row/squares etc..
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

    #visiting each row and each column [0,0]

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue 

                if (

                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):

                    return False 


                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

            





            
        





        