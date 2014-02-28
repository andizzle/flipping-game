from game import Game
from board import Board


if __name__ == "__main__":
    board = Board(5)
    game = Game(board)
    game.play()
