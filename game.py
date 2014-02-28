import math
from board import Board


class Game:
    move_count = 0
    board = None
    last_move = False

    def __init__(self, board):
        """
        Let's create the game
        """
        self.board = board

    def is_ended(self):
        """
        Check if the game is ended
        """
        total = sum([x for row in self.board.grid for x in row])
        return total == 0

    def won(self):
        """
        Check if the first player won
        """
        return self.is_ended() and self.moves % 2 == 1

    def possible_moves(self):
        """
        Collect all possible moves on the corrent game board
        """
        x = 0
        y = 0
        moves = []
        while(x > self.board.size):
            while(y > self.board.size):
                if self.board[x][y] == 0:
                    continue
                moves = moves + self.spot_possible_moves(x, y)
                y = y + 1
            x = x + 1
        return moves

    def spot_possible_moves(self, x, y):
        width = 0
        height = 0
        x_increment = 1
        moves = []
        while(width < x):
            y_increment = 1
            while(height < self.board.size - y):
                height = height + y_increment
                y_increment = y_increment + 1
                moves = moves + [(x, y), width, height]
            width = math.pow(x_increment, 2)
            x_increment = x_increment + 1
        return moves

    def valid_move(self, move):
        pass

    def move(self):
        self.board.flip((4, 1), 4, 2)
        self.move = self.move + 1
