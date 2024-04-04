class Board:
    def __init__(self):
        self.board = [[None, None, None, None, 4, None, 6, None, None, None, None],
                      [None, None, None, 3, None, 5, None, 7, None, None, None],
                      [None, None, 2, None, 4, None, 6, None, 8, None, None],
                      [None, 1, None, 3, None, 5, None, 7, None, 9, None],
                      [None, None, 2, None, 4, None, 6, None, 8, None, None],
                      [None, 1, None, 3, None, 5, None, 7, None, 9, None],
                      [0, None, 2, None, 4, None, 6, None, 8, None, 10],
                      [None, 1, None, 3, None, 5, None, 7, None, 9, None],
                      [0, None, 2, None, 4, None, 6, None, 8, None, 10],
                      [None, 1, None, 3, None, 5, None, 7, None, 9, None],
                      [0, None, 2, None, 4, None, 6, None, 8, None, 10],
                      [None, 1, None, 3, None, 5, None, 7, None, 9, None],
                      [0, None, 2, None, 4, None, 6, None, 8, None, 10],
                      [None, 1, None, 3, None, 5, None, 7, None, 9, None],
                      [None, None, 2, None, 4, None, 6, None, 8, None, None],
                      [None, 1, None, 3, None, 5, None, 7, None, 9, None],
                      [None, None, 2, None, 4, None, 6, None, 8, None, None],
                      [None, None, None, 3, None, 5, None, 7, None, None, None],
                      [None, None, None, None, 4, None, 6, None, None, None, None]]

    def __str__(self):
        board_str = ''
        for row in self.board:
            board_str += ' '.join([str(cell) if cell is not None else ' ' for cell in row]) + '\n'
        return board_str

if __name__ == '__main__':
    board = Board()
    print(board)