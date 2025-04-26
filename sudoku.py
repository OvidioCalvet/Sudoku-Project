# Imports
from sudoku_generator import SudokuGenerator, generate_sudoku
from board import Board
from cell import Cell
import pygame, sys

# Final Variables
WIDTH: int = 800
HEIGHT: int  = 800
BUTTON_COLOR = 111, 130, 106
BACKGROUND_COLOR = 187, 216, 163
TEXT_COLOR = 240, 241, 197

# Funcitons
def draw_welcome_screen(screen):
    # Initialize fonts
    title_font = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 70)
    
    # Sets the screens background color to custom pallete
    screen.fill(BACKGROUND_COLOR)

    # Draw the title surface
    title = title_font.render("SUDOKU", 0, TEXT_COLOR)
    title_container = title.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title, title_container)

    # Draw the "easy" button surface
    easy_button = button_font.render("EASY", 0, TEXT_COLOR)
    easy_button_container = easy_button.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(easy_button, easy_button_container)

    # Draw the "medium" button surface
    medium_button = button_font.render("MEDIUM", 0, TEXT_COLOR)
    medium_button_container = medium_button.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(medium_button, medium_button_container)

    # Draw the "hard" button surface
    hard_button = button_font.render("HARD", 0, TEXT_COLOR)
    hard_button_container = hard_button.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(hard_button, hard_button_container)

def draw_game_screen():
    pass

def draw_win_screen():
    pass

def draw_lose_screen():
    pass

# Main function where the screen and event handling is done
if __name__ == "__main__":

    # Pygame screen setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SUDOKU")
    clock = pygame.time.Clock()

    # Welcome screen
    draw_welcome_screen(screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update Everything
        pygame.display.update()
        # Limits screen at 60 fps
        clock.tick(60)