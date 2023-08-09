import math,random


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):  # class attributes
        self.row_length = row_length  # length of each row (9)
        self.removed_cells = removed_cells  # total num of cells to be removed
        # 2D list of 0s forming square of board
        self.board = [[0 for i in range(row_length)] for j in range(9)]
        self.box_length = int(math.sqrt(row_length))  # length of 1 sudoku box
        self.solution = None

    def get_board(self):  # returns 2D list board
        return self.board

    def print_board(self):  # displays the board for debug purposes
        for row in self.board:
            print(row, end='\n')
        return

    def valid_in_row(self, row, num):
        for number in self.board[row]:  # iterate through a specified row
            if number == num:  # check each number in row for val: num
                return False  # if num exists return False
        return True  # otherwise num is valid in row

    def valid_in_col(self, col, num):
        for x in range(9):  # iterate through entire column range
            if self.board[x][col] == num:  # check each board[x][col] for value of num
                return False  # if the col has num then it is not valid
        return True  # otherwise the number is valid in the column

    def valid_in_box(self, row_start, col_start, num):
        for i in range(self.box_length):  # iterate through box height
            for j in range(self.box_length):  # iterate through box length
                if self.board[row_start + i][col_start + j] == num:  # check for number throughout box
                    return False
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3,
                                                                                             col - col % 3, num):
            return True
        return False

    def solve(self, row, col):
        if row == 9:
            return True

        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)

        if self.board[row][col] != 0:
            return self.solve(next_row, next_col)

        for num in range(9):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve(next_row, next_col):
                    return True
                self.board[row][col] = 0

        return False

    def fill_box(self, row_start, col_start):
        for i in range(3):
            for j in range(3):
                x = random.randint(1, 9)
                if not self.valid_in_box(row_start, col_start, x):
                    self.board[row_start + i][col_start + j] = x
        return

    def fill_diagonal(self):
        for i in range(0, 9, 3):
            self.fill_box(i, i)
        return

    def fill_remaining(self, row, col):  # call after diagonal boxes are filled
        if row == self.row_length - 1 and col == self.row_length:
            return True
        if col == self.row_length:
            row += 1
            col = 0
        if self.board[row][col] != 0:
            return self.fill_remaining(row, col + 1)
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # Constructs a solution by calling fill_diagonal and fill_remaining
        self.fill_diagonal()
        self.fill_remaining(0, 3)
        self.solution = [row[:] for row in self.board]

    def remove_cells(self):  # call after fill values is called
        while self.removed_cells > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                self.removed_cells -= 1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.remove_cells()
    sudoku.print_board()
    return sudoku

