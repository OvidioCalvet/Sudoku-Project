import pygame
from final_variables import *


class Cell:

    def __init__(self, value, row, col, screen, is_correct=True, filled=False): #default values for correct and filled so code works properly.

        self.sketched_value = 0  # temp value shown before confirmation
        self.selected = False
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.is_correct = is_correct
        self.filled = filled

    def set_cell_value(self, value):
        if not self.filled:
            self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        # set position
        x = X_OFFSET + CELL_SIZE * self.col 
        y = Y_OFFSET + CELL_SIZE * self.row

        # Create fonts
        font = pygame.font.Font(None, 40)
        sketch_font = pygame.font.Font(None, 25)

        # draw the regular border
        pygame.draw.rect(self.screen, CELL_BORDER, (x, y, CELL_SIZE, CELL_SIZE), 2)
        # draw the red outline if selected
        if self.selected:
            pygame.draw.rect(self.screen, OUTLINE_COLOR, (x, y, CELL_SIZE, CELL_SIZE), 2)

        # draw the filled numbers
        if self.value != 0:
            # pre-filled stays TEXT_COLOR, user input is always grey
            color = TEXT_COLOR if self.filled else (128, 128, 128)
            num = font.render(str(self.value), True, color)
            text_rectangle = num.get_rect(center=(x + CELL_SIZE//2, y + CELL_SIZE//2))
            self.screen.blit(num, text_rectangle)

        # 4) pencil mark if no permanent value
        elif self.sketched_value != 0:
            num = sketch_font.render(str(self.sketched_value), True, (120, 120, 120))
            text_rectangle = num.get_rect(center=(x + CELL_SIZE//2, y + CELL_SIZE//2))
            self.screen.blit(num, text_rectangle)

