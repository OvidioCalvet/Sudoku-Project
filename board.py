import pygame
from cell import Cell
from sudoku_generator import *
from final_variables import *


class Board:

    def __init__(self, width, height, screen, difficulty):

        self.screen = screen
        self.difficulty = difficulty
        self.width = width
        self.height = height
        self.selected = None
        self.solution = []
        self.cells = []

        removed = 0
        # removed variable for generate_sudoku function
        if difficulty == "easy":
            removed = 30
        elif difficulty == "medium":
            removed = 40
        else:
            removed = 50

        puzzle = SudokuGenerator(self.width, removed)
        puzzle.fill_values()
        self.solution = [row[:] for row in puzzle.get_board()]

        # populate self.cells
        temp = []
        for row in range(self.width):
            for col in range(self.height):
                cell = Cell(0, row, col, self.screen)
                temp.append(cell)
            self.cells.append(temp)
            temp = []

        # Complete Setup
        self.puzzle = puzzle
        self.puzzle.remove_cells()
        board = self.puzzle.get_board()

        # snapshot of puzzle with zeroes
        self.starting_board = [row[:] for row in puzzle.get_board()]

        # Turn into Cells
        for row in range(self.width):
            for col in range(self.height):
                value = board[row][col]
                filled = value != 0
                self.cells[row][col] = Cell(value, row, col, screen, filled=filled)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        cell_size = 60
        for row in range(self.width):
            for col in range(self.height):
                self.cells[row][col].draw()

        for i in range(0, 10, 3):
            pygame.draw.line(
                self.screen,
                TEXT_COLOR,
                (X_OFFSET + i * CELL_SIZE, Y_OFFSET),
                (X_OFFSET + i * CELL_SIZE, Y_OFFSET + CELL_SIZE * 9 + LINE_WIDTH),
                LINE_WIDTH + 1,
            )

            pygame.draw.line(
                self.screen,
                TEXT_COLOR,
                (X_OFFSET, Y_OFFSET + i * CELL_SIZE),
                (X_OFFSET + CELL_SIZE * 9 + LINE_WIDTH, Y_OFFSET + i * CELL_SIZE),
                LINE_WIDTH + 1,
            )

    def select(self, row, col):
        # un‐select old
        if self.selected:
            r_old, c_old = self.selected
            self.cells[r_old][c_old].selected = False

        # select new
        self.selected = (row, col)
        self.cells[row][col].selected = True

    def click(self, x, y):
        if (
            X_OFFSET <= x < X_OFFSET + GRID_SIZE
            and Y_OFFSET <= y < Y_OFFSET + GRID_SIZE
        ):
            col = (x - X_OFFSET) // CELL_SIZE
            row = (y - Y_OFFSET) // CELL_SIZE
            self.select(int(row), int(col))
            return (int(row), int(col))
        
        return None

    def clear(self):
        if self.selected:
            row, col = self.selected
            cell = self.cells[row][col]
            if not cell.filled:
                cell.set_cell_value(0)
                cell.is_correct = True

    def sketch(self, value):
        if self.selected:
            row, col = self.selected
            cell = self.cells[row][col]
            if not cell.filled:
                cell.sketched_value(value)

    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            cell = self.cells[row][col]
            if not cell.filled:
                cell.set_cell_value(value)
                cell.is_correct = (value == self.solution[row][col])
                return True
            
        return False

    def reset_to_original(self):
        for row in range(self.height):
            for col in range(self.width):
                original_value = self.starting_board[row][col]

                cell = self.cells[row][col]
                cell.is_correct = True
                cell.sketched_value = 0

                if original_value == 0:
                    cell.set_cell_value(0)
                    cell.filled = False
                else:
                    cell.set_cell_value(original_value)
                    cell.filled = True
                        
    def is_full(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        for row in range(self.height):
            for col in range(self.width):
                self.puzzle[row][col] = self.cells[row][col].value

    def find_empty(self):

        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        if not self.is_full():
            return False
        return all(
            self.cells[row][col].value == self.solution[row][col]
            for row in range(self.height)
            for col in range(self.width)
        )