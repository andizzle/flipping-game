class Board:

    grid = []
    size = 0

    def __init__(self, board_size):
        """
        Construct a board grid like
        """
        x = 0
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

    def flip_row(self, row, start, cycle):
        """
        Flip a single row
        """
        while(cycle >= 0):
            self.grid[row][cycle] = 1 if self.grid[row][cycle] == 0 else 0
            cycle = cycle - 1

    def flip(self, upper_right, width, height):
        """
        Flip the board within the range
        e.g, upper_right = (1, 4)
        """
        x = upper_right[0]
        y = upper_right[1]
        while(x - height > 0):
            self.flip_row(height - y, width, width - y)
            height = height + 1
