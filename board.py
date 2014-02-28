from Move import move


class Board:

    size = 0
    moves = 0

    def __init__(self, board_size):
        """
        Construct a board grid like
        """
        x = 0
        self.grid = []
        self.size = board_size
        while(x < board_size):
            row = [1 for size in range(board_size)]
            self.grid.append(row)
            x = x + 1

    def print_grid(self):
        """
        Print the game board like a board
        """
        print '-' * len(self.grid) * 3
        for x in self.grid:
            print x
        print '-' * len(self.grid) * 3

    def flip(self, move):
        """
        Flip the board within the range
        e.g, upper_right = (3, 0)
        """
        upper_right = move.upper_right
        width = move.width
        height = move.height
        self.moves = self.moves + 1
        x = upper_right[0]
        while(width > 0):
            y = upper_right[1]
            width = width - 1
            loop_height = height
            while(loop_height > 0):
                loop_height = loop_height - 1
                self.grid[y][x] = 1 if self.grid[y][x] == 0 else 0
                y = y + 1
            x = x - 1
