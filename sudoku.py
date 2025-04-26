# Imports
from sudoku_generator import SudokuGenerator
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

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button_container.collidepoint(event.pos):
                    return "easy"
                elif medium_button_container.collidepoint(event.pos):
                    return "medium"
                elif hard_button_container.collidepoint(event.pos):
                    return "hard"
                
        pygame.display.update()

def draw_game_screen(screen, difficulty):
    # Innitialize Fonts
    button_font = pygame.font.Font(None, 70)

    board = Board(width=9, height=9, screen=screen, difficulty=difficulty)

    # Draw the "reset" button surface
    reset_button = button_font.render("RESET", 0, TEXT_COLOR)
    reset_button_container = reset_button.get_rect(center = (WIDTH // 2 - 300, HEIGHT // 2 + 350))
    screen.blit(reset_button, reset_button_container)

    # Draw the "restart" button surface
    restart_button = button_font.render("RESTART", 0, TEXT_COLOR)
    restart_button_container = restart_button.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 350))
    screen.blit(restart_button, restart_button_container)

    # Draw the "exit" button surface
    exit_button = button_font.render("EXIT", 0, TEXT_COLOR)
    exit_button_container = exit_button.get_rect(center = (WIDTH // 2 + 300, HEIGHT // 2 + 350))
    screen.blit(exit_button, exit_button_container)

    while True:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button_container.collidepoint(event.pos):
                        sys.exit()
                    elif reset_button_container.collidepoint(event.pos):
                        return "win"
                    elif restart_button_container.collidepoint(event.pos):
                        return "lose"
        pygame.display.update()

def draw_win_screen(screen):
    # Initialize fonts
    title_font = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 70)
    
    # Sets the screens background color to custom pallete
    screen.fill(BACKGROUND_COLOR)

    # Draw the title surface
    title = title_font.render("YOU WON!", 0, TEXT_COLOR)
    title_container = title.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title, title_container)

    # Draw the "exit" button surface
    exit_button = button_font.render("EXIT", 0, TEXT_COLOR)
    exit_button_container = exit_button.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(exit_button, exit_button_container)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_container.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

def draw_lose_screen(screen):
    # Initialize fonts
    title_font = pygame.font.Font(None, 200)
    button_font = pygame.font.Font(None, 70)
    
    # Sets the screens background color to custom pallete
    screen.fill(BACKGROUND_COLOR)

    # Draw the title surface
    title = title_font.render("YOU LOST!", 0, TEXT_COLOR)
    title_container = title.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title, title_container)

    # Draw the "restart" button surface
    restart_button = button_font.render("RESTART", 0, TEXT_COLOR)
    restart_button_container = restart_button.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_button, restart_button_container)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button_container.collidepoint(event.pos):
                    return "easy"
        pygame.display.update()

# Main function where the screen and event handling is done
if __name__ == "__main__":

    # Pygame screen setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SUDOKU")
    clock = pygame.time.Clock()

    # Welcome screen
    difficulty = draw_welcome_screen(screen)

    # Refresh's screen
    screen.fill(BACKGROUND_COLOR)

    # Game screen
    status = draw_game_screen(screen, difficulty)

    # End screen
    if status == "win":
        draw_win_screen(screen)

    elif status == "lose":
        draw_lose_screen(screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update Everything
        pygame.display.update()
        # Limits screen at 60 fps
        clock.tick(60)