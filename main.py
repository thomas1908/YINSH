class Case:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def set__Value(self, value):
        self.value = value

    def get__Value(self):
        return self.value
    def __str__(self):
        return f'Case({self.x}, {self.y}, {self.value})'

class Board:
    def __init__(self):
        self.board = [[None, None, None, None, Case, None, Case, None, None, None, None],
                      [None, None, None, Case, None, Case, None, Case, None, None, None],
                      [None, None, Case, None, Case, None, Case, None, Case, None, None],
                      [None, Case, None, Case, None, Case, None, Case, None, Case, None],
                      [None, None, Case, None, Case, None, Case, None, Case, None, None],
                      [None, Case, None, Case, None, Case, None, Case, None, Case, None],
                      [Case, None, Case, None, Case, None, Case, None, Case, None, Case],
                      [None, Case, None, Case, None, Case, None, Case, None, Case, None],
                      [Case, None, Case, None, Case, None, Case, None, Case, None, Case],
                      [None, Case, None, Case, None, Case, None, Case, None, Case, None],
                      [Case, None, Case, None, Case, None, Case, None, Case, None, Case],
                      [None, Case, None, Case, None, Case, None, Case, None, Case, None],
                      [Case, None, Case, None, Case, None, Case, None, Case, None, Case],
                      [None, Case, None, Case, None, Case, None, Case, None, Case, None],
                      [None, None, Case, None, Case, None, Case, None, Case, None, None],
                      [None, Case, None, Case, None, Case, None, Case, None, Case, None],
                      [None, None, Case, None, Case, None, Case, None, Case, None, None],
                      [None, None, None, Case, None, Case, None, Case, None, None, None],
                      [None, None, None, None, Case, None, Case, None, None, None, None]]

    def __str__(self):
        board_str = ''
        for row in self.board:
            board_str += ' '.join([str('◉') if cell is not None else ' ' for cell in row]) + '\n'
        return board_str

    def getCase(self, x, y):
        return self.board[y][x]

    def setCase(self, x, y, value):
        self.board[y][x] = value

if __name__ == '__main__':
    board = Board()
    print(board)
    board.getCase(4, 0).set__Value(2)
    print(board.getCase(4, 0).get__Value())
    print(board)