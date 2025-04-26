from pygame import *
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

        self.board_values = generate_sudoku(9,removed)

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
        #         x = col * cell_size
        #         y = row * cell_size
        #         pygame.draw.rect(self.screen, (200, 200, 200), (x, y, cell_size, cell_size), 1)
        #
        # pygame.display.update()
