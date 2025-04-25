from pygame import *
from sudoku_generator import generate_sudoku

class Board:

    def __init__(self, width, height, screen, difficulty):

        self.screen = screen
        self.difficulty = difficulty
        self.width = width
        self.height = height

        if difficulty == "easy":
            removed = 30
        elif difficulty == "medium":
            removed = 40
        else:
            removed = 50

        self.board_values = generate_sudoku(9,removed)

        self.cells = []

        for row in range(9):
            self.cells.append([])
            for col in range(9):
                values = self.board_values[row][col]
                cell = Cell(values,row,col,screen)
                self.cells[row].append(cell)

        self.selected = None

    def draw(self):
        pass