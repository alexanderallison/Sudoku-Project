import pygame
from cell import *
from board import *
from sudoku_generator import *

# Initialize pygame
pygame.init()

# Define some constants for the game
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Font for the menu
menu_font = pygame.font.Font(None, 48)

# Difficulty levels and corresponding empty cell counts
DIFFICULTY_LEVELS = {
    "easy": 30,
    "medium": 40,
    "hard": 50
}


# Display the difficulty selection menu
def show_menu():
    while True:
        SCREEN.fill((255, 255, 255))
        for i, (level, _) in enumerate(DIFFICULTY_LEVELS.items()):
            text = menu_font.render(f"{i + 1}. {level.capitalize()}", True, (0, 0, 0))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))
            SCREEN.blit(text, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    for i, (_, cell_count) in enumerate(DIFFICULTY_LEVELS.items()):
                        if (WIDTH // 2 - 100) < x < (WIDTH // 2 + 100) and \
                                (HEIGHT // 2 - 25 + i * 50) < y < (HEIGHT // 2 + 25 + i * 50):
                            return cell_count


# Show the difficulty selection menu and get the chosen difficulty
chosen_difficulty = show_menu()

# Map the chosen difficulty to the corresponding key in DIFFICULTY_LEVELS
difficulty_key = None
for key, value in DIFFICULTY_LEVELS.items():
    if value == chosen_difficulty:
        difficulty_key = key
        break

# Create an instance of the SudokuGenerator class to generate the board
sudoku_generator = SudokuGenerator.generate_sudoku(9, DIFFICULTY_LEVELS[difficulty_key])
#sudoku_generator.generate_sudoku()

# Create an instance of the Board class with the generated board
board = Board(WIDTH, HEIGHT, SCREEN, difficulty_key)

# Font for the winning message
win_font = pygame.font.Font(None, 36)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                board.click(x, y)
        elif event.type == pygame.KEYDOWN:
            if board.selected_cell:
                if event.unicode.isdigit():
                    value = int(event.unicode)
                    if value >= 1 and value <= 9:
                        board.place_number(value)
                elif event.key == pygame.K_RETURN:
                    if board.selected_cell.sketched_value != 0:
                        board.place_number(board.selected_cell.sketched_value)
                        board.selected_cell.set_sketched_value(0)

    SCREEN.fill((255, 255, 255))

    # Draw vertical and horizontal lines to visually divide the smaller boxes
    cell_size = WIDTH // 9
    for i in range(1, 9):
        color = (0, 0, 0) if i % 3 == 0 else (150, 150, 150)
        pygame.draw.line(SCREEN, color, (i * cell_size, 0), (i * cell_size, HEIGHT))
        pygame.draw.line(SCREEN, color, (0, i * cell_size), (WIDTH, i * cell_size))

    board.draw()

    if board.is_full() and board.check_board():
        win_text = win_font.render("Congratulations! You've solved the puzzle.", True, (0, 0, 0))
        win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT - 30))
        SCREEN.blit(win_text, win_rect)

    pygame.display.update()

pygame.quit()
