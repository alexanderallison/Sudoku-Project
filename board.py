from sudoku_generator import SudokuGenerator
from cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen  # window from Pygame
        self.difficulty = difficulty  # variable from user input
        # instantiate 81 cells:
        self.cells = [[Cell(0, row, col, self.screen) for col in range(9)] for row in range(9)]
        # instantiate sudoku 2D list
        self.sudoku_generator.generate_sudoku(9, self.difficulty)
        self.selected_cell = None

    def draw(self):  # draw outline of sudoku grid with lines
        for row in self.cells:
            for cell in row:
                cell.draw()
        # draw every cell

    def select(self, row, col): # marks row, col as current cell selection
        # allows user to edit value of selected cell
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):  # returns a tuple of coordinates of clicked cell
        # if coordinate not in board return None
        row = y // (self.height // 9) # find the row, col of clicked cell
        col = x // (self.width // 9)
        if (-1 < row < 9) and (-1 < col < 9):  # check if on board
            select_coord = tuple(row, col)
            return select_coord
        return None

    def clear(self):
        # clears value of a user selected cell
        if self.selected_cell:
        pass

    def sketch(self, value):
        #  sets sketched value of selected cell to user input
        # displays the value at the top corner of cell
        pass

    def place_number(self, value):
        # sets the value of current cell to user input
        # called when user presses enter key
        pass

    def reset_to_original(self):
        # resets all cells to original values (0 if removed)
        pass

    def is_full(self):
        # checks board and returns True if all cells are no 0
        pass

    def update_board(self):
        # updates the 2D board list with values of all cells
        pass

    def find_empty(self):
        # finds an empty cell and returns its row and col as tuple (x,y)
        pass

    def check_board(self):
        # checks whether the board is solved correctly
        pass


