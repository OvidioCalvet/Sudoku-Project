# Imports
from sudoku_generator import SudokuGenerator
from final_variables import *
from board import Board
import pygame, sys

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
    # pre-render fonts
    button_font = pygame.font.Font(None, 70)
    board = Board(BOARD_WIDTH, BOARD_WIDTH, screen, difficulty)

    # pre‐render buttons before blit
    reset_surf   = button_font.render("RESET",   True, TEXT_COLOR)
    restart_surf = button_font.render("RESTART", True, TEXT_COLOR)
    exit_surf    = button_font.render("EXIT",    True, TEXT_COLOR)

    # buttons surfaces
    reset_rect   = reset_surf.get_rect(center=(WIDTH//2 - 300, HEIGHT//2 + 350))
    restart_rect = restart_surf.get_rect(center=(WIDTH//2,     HEIGHT//2 + 350))
    exit_rect    = exit_surf.get_rect(   center=(WIDTH//2 + 300, HEIGHT//2 + 350))

    # resetting variable
    resetting = False

    while True:

        screen.fill(BACKGROUND_COLOR)
        board.draw()

        # draw buttons on top
        screen.blit(reset_surf,   reset_rect)
        screen.blit(restart_surf, restart_rect)
        screen.blit(exit_surf,    exit_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # — mouse clicks —
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                # UI buttons
                if exit_rect.collidepoint(mx, my):
                    pygame.quit(); sys.exit()
                elif reset_rect.collidepoint(mx, my):
                    board.reset_to_original()
                    resetting = True
                elif restart_rect.collidepoint(mx, my):
                    return "restart"
                else:
                    # grid click! calls board.select() internally
                    board.click(mx, my)

            # — keys —
            elif event.type == pygame.KEYDOWN:
                # clear
                if event.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                    board.clear()

                # place 1–9
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    board.place_number(event.key - pygame.K_0)

                # arrow movement
                elif event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    if board.selected is None:
                        board.select(0, 0)
                    else:
                        row, col = board.selected
                        if event.key == pygame.K_UP    and row > 0:            
                            board.select(row - 1, col)
                        if event.key == pygame.K_DOWN  and row < BOARD_WIDTH-1: 
                            board.select(row + 1, col)
                        if event.key == pygame.K_LEFT  and col > 0:             
                            board.select(row, col - 1)
                        if event.key == pygame.K_RIGHT and col < BOARD_WIDTH-1: 
                            board.select(row, col + 1)

        # end‐of‐game
        if not resetting and board.is_full():
            return "win" if board.check_board() else "lose"

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
                    return "exit"
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
                    return "restart"
        pygame.display.update()

# Main function where the screen and event handling is done
if __name__ == "__main__":

    # Pygame screen setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SUDOKU")
    clock = pygame.time.Clock()

    while True:

            # Welcome screen
        difficulty = draw_welcome_screen(screen)

        # Refresh's screen
        screen.fill(BACKGROUND_COLOR)

        # Game screen
        status = draw_game_screen(screen, difficulty)

        if status in ("exit", "restart"):
            continue

        # Win screen
        if status == "win":
            draw_win_screen(screen)

        # Lose screen
        elif status == "lose":
            draw_lose_screen(screen)