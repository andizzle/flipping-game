import copy
import math


class Move:
    """
    A move is consists of flipping all disks in a rectangle with the
    following properties:

    the upper right corner of the rectangle contains a white disk
    the rectangle width is a perfect square (1, 4, 9, 16, ...)
    the rectangle height is a triangular number (1, 3, 6, 10, ...)
    """

    rank = 0

    def __init__(self, game, starting_point, width, height):
        self.game = game
        self.board = game.board
        self.starting_point = starting_point
        self.width = width
        self.height = height

    def grid_valid_moves(self, x, y, queue=None):
        """
        Given a spot on the grid, get all possible moves
        """
        moves = []
        width = 1
        x_increment = 2
        while(width <= self.board.size and x - width + 1 >= 0):
            y_increment = 2
            height = 1
            while(height <= self.board.size - y and y + height <= self.board.size):
                move = Move(copy.deepcopy(self.board), (x, y), width, height)
                moves.append(move)
                height = height + y_increment
                y_increment = y_increment + 1
            width = int(math.pow(x_increment, 2))
            x_increment = x_increment + 1
        if queue is not None:
            queue.put(moves)
        return moves

    def possible_moves(self):
        """
        Collect all possible moves on the current game board
        """
        moves = []
        x = 0
        while(x < self.board.size):
            y = 0
            while(y < self.board.size):
                if self.board.grid[y][x] == 0:
                    y = y + 1
                    continue
                moves = moves + self.grid_valid_moves(x, y)
                y = y + 1
            x = x + 1
        return moves

    def next_best_moves(self):
        """
        Get next number of best moves, minimum 1
        """
        moves = self.possible_moves()
        for move in moves:
            pass

    def get_next_best_move(self, move):
        """
        Play the game, get all possible first moves, and start mini games
        """
        self.game.play(move)

    def move(self, next_move):
        self.board.flip(next_move)
        return self.board
