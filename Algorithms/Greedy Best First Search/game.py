from random import shuffle

class Game:

    def __init__(self):
        """Return the inital state of the board."""
        x = list(range(1, 9))
        x.append('X')
        shuffle(x)
        self.terminal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 'X']]
        self.board = [x[0:3], x[3:6], x[6:]]
        # TEST CASE. 58 STEPS TO SOLVE & 1188 ITERATIONS
        # self.board = [[3, 2, 4], [7, 8, 6], ['X', 1, 5]]

    def exec_UP(self):
        """Execute the move up."""
        r, c = self._pos()
        tmp = self.board[r - 1][c]
        self.board[r - 1][c] = 'X'
        self.board[r][c] = tmp

    def exec_DOWN(self):
        """Execute the move down."""
        r, c = self._pos()
        tmp = self.board[r + 1][c]
        self.board[r + 1][c] = 'X'
        self.board[r][c] = tmp

    def exec_RIGHT(self):
        """Execute the move right."""
        r, c = self._pos()
        tmp = self.board[r][c + 1]
        self.board[r][c + 1] = 'X'
        self.board[r][c] = tmp

    def exec_LEFT(self):
        """Execute the move left."""
        r, c = self._pos()
        tmp = self.board[r][c - 1]
        self.board[r][c - 1] = 'X'
        self.board[r][c] = tmp

    def _pos(self):
        """Return position of player on the board."""
        for row in range(0, 3):
            for column in range(0, 3):
                if self.board[row][column] == "X":
                    return row, column


    def __str__(self):
        return (f"""
                {self.board[0][0]} || {self.board[0][1]} || {self.board[0][2]}
                ============
                {self.board[1][0]} || {self.board[1][1]} || {self.board[1][2]}
                ============
                {self.board[2][0]} || {self.board[2][1]} || {self.board[2][2]}""")


