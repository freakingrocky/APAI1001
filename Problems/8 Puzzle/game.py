from random import shuffle

class Game:
    
    def __init__(self):
        """Return the inital state of the board."""
        x = list(range(1, 9))
        x.append('X')
        shuffle(x)
        self.board = [x[0:3], x[3:6], x[6:]]

    def terminal_state(self):
        """Return True if game has ended, False otherwise."""
        terminal_board = [[1, 2, 3], [3, 5, 6], [7, 8, 'X']]
        return True if self.board == terminal_board else False

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

    def UP(self):
        """Returnt he result of the move up."""
        r, c = self._pos()
        tmp = self.board[r - 1][c]
        b = self.board
        b[r - 1][c] = 'X'
        b[r][c] = tmp
        return b

    def DOWN(self):
        """Returnt he result of the move down."""
        r, c = self._pos()
        tmp = self.board[r + 1][c]
        b = self.board
        b[r + 1][c] = 'X'
        b[r][c] = tmp
        return b

    def RIGHT(self):
        """Returnt he result of the move right."""
        r, c = self._pos()
        tmp = self.board[r][c + 1]
        b = self.board
        b[r][c + 1] = 'X'
        b[r][c] = tmp
        return b

    def LEFT(self):
        """Return the result of the move left."""
        r, c = self._pos()
        tmp = self.board[r][c - 1]
        b = self.board
        b[r][c - 1] = 'X'
        b[r][c] = tmp
        return b

    def _pos(self):
        """Return position of player on the board."""
        for row in range(0, 3):
            for column in range(0, 3):
                if self.board[row][column] == "X":
                    return row, column

    def available_moves(self):
        """Return set of available moves."""
        row, column = self._pos()
        moves = set()
        if row != 2:
            moves.add('DOWN')
        if row != 0:
            moves.add('UP')
        if column != 0:
            moves.add('LEFT')
        if column != 2:
            moves.add('RIGHT')
        return moves

    def __str__(self):
        return (f"""
                {self.board[0][0]} || {self.board[0][1]} || {self.board[0][2]}
                ============
                {self.board[1][0]} || {self.board[1][1]} || {self.board[1][2]}
                ============
                {self.board[2][0]} || {self.board[2][1]} || {self.board[2][2]}""")


