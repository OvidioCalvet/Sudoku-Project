import pygame


class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0  # temp value shown before confirmation
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        # draws this cell, along with the value inside it
        cell_size = 540 // 9
        x = self.col * cell_size
        y = self.row * cell_size

        # Creates a font to draw the final value
        font = pygame.font.SysFont("comicsans", 40)

        if self.value != 0:  # not 0 value is displayed
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 10))

        elif self.sketched_value != 0:  # displays sketched value
            sketch_font = pygame.font.SysFont("comicsans", 25)
            sketch = sketch_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(sketch, (x + 5, y + 5))
        # outlines cell in red
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)
