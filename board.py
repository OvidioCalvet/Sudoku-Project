from pygame import *
from cell import Cell
from sudoku_generator import generate_sudoku
from cell import *

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

        self.board_values = generate_sudoku(9, removed)

        self.cells = []

        for row in range(9):
            self.cells.append([])
            for col in range(9):
                value = self.board_values[row][col]
                cell = Cell(value,row,col,screen)
                self.cells[row].append(cell)

        self.selected = None

    def draw(self):
        self.screen.fill((255, 255, 255))
        cell_size = 60
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, self.height), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * cell_size), (self.width, i * cell_size), line_width)

    def select(self, row, col):
        self.selected = (row, col)
        return self.selected

    def click(self, x, y):
        pass

    def clear(self):
        if self.selected:
            row, col = self.selected
            self.cells[row][col].cell_value(0)

    def sketch(self, value):
        if self.selected:
            row, col = self.selected
            self.cells[row][col].sketched_value(value)

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        for row in range(self.height):
            for col in range(self.width):
                if Cell.value == 0:
                    return False
        return True

    def update_board(self):
        for row in range(self.height):
            for col in range(self.width):
                self.board_values[row][col] = self.cells[row][col].value

    def find_empty(self):

        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        pass