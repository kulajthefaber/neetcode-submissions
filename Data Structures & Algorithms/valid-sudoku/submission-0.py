class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_vals = "123456789."
        length = len(board)

        #check rows
        for i in range(length):
            cur_vals = []
            for j in range(length):
                val = board[i][j]
                if val not in valid_vals:
                    return False
                elif val not in cur_vals:
                    cur_vals.append(val)
                elif val in cur_vals and val!=".":
                    return False
        

        #check cols
        for j in range(length):
            cur_vals = []
            for i in range(length):
                val = board[i][j] 
                if val not in valid_vals:
                    return False
                elif val not in cur_vals:
                    cur_vals.append(val)
                elif val in cur_vals and val!=".":
                    return False
                

        # Outer loops replace the hard-coded matrix array
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                curr_subb = []
                
                # Inner loops check each 3x3 subgrid
                for ii in range(3):
                    for jj in range(3):
                        fi = x + ii
                        si = y + jj
                        val = board[fi][si]
                        
                        if val not in curr_subb:
                            curr_subb.append(val)
                        elif val in curr_subb and val != ".":
                            return False


        return True
        #check subcols
