class Board:
    def __init__(self):
        self.board = [['o' for _ in range(11)] for _ in range(11)]

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.board)


if __name__ == '__main__':
    board = Board()
    print(board)
