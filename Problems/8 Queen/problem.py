from random import randint


class Problem:
    
    def __init__(self):
        self.board = []
        for _ in range(8):
            pos = randint(0, 8)
            row = []
            for j in range(8):
                if j == pos:
                    row.append(1)
                else:
                    row.append(0)
            self.board.append(row)


    def __str__(self):
        str_board = "     0   1   2   3   4   5   6   7  \n" + f"{'='*36}\n"
        for row in range(8):
            str_board += f"{row}  "
            for column in self.board[row]:
                str_board += "|   " if column == 0 else "| X "
            str_board += f'|\n{"="*36}\n'
        return str_board

