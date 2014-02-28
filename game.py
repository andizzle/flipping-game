import copy
import math
from multiprocessing import Process, Queue
from board import Board


class Game:
    workers = 600
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
        return self.is_ended() and self.move_count % 2 == 1

    def reach_last_move(self):
        self.last_move = True

    def possible_moves(self):
        """
        Collect all possible moves on the current game board
        """
        moves = []
        points = []
        x = 0
        while(x < self.board.size):
            y = 0
            while(y < self.board.size):
                if self.board.grid[x][y] == 0:
                    y = y + 1
                    continue
                points.append([x, y])
                y = y + 1
            x = x + 1

        point_range = range(0, len(points), self.workers)
        for points_set in [points[i:i + self.workers] for i in point_range]:
            queue = Queue()
            processes = []
            for w in xrange(len(points_set)):
                x = points_set[w][0]
                y = points_set[w][1]
                p = Process(target=self.spot_possible_moves, args=(x, y, queue))
                p.start()
                processes.append(p)

            for process in processes:
                moves = moves + queue.get()
                process.join()
        return moves

    def spot_possible_moves(self, x, y, queue=None):
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
                moves.append([(x, y), width, height])
                height = height + y_increment
                y_increment = y_increment + 1
            width = int(math.pow(x_increment, 2))
            x_increment = x_increment + 1
        if queue is not None:
            queue.put(moves)
        return moves

    def move(self, upper_right, width, height):
        """
        Make a move, increase the move count
        """
        self.board.flip(upper_right, width, height)
        self.move_count = self.move_count + 1

