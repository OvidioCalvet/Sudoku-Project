import math, random


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):

        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []

        temp = []
        for i in range(self.row_length):
            for j in range(self.row_length):
                temp.append(0)
            self.board.append(temp)
            temp = []
            
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(self.board[row])

    def valid_in_row(self, row, num):
        for i in self.board[row]:
            if i == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for row in self.board:
            if row[int(col)] == num:
                return False
        return True

    def valid_in_box(self, row, col, num):
        box_row = row - (row % 3)
        box_col = col - (col % 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (
        self.valid_in_row(row, num)
        and self.valid_in_col(col, num)
        and self.valid_in_box(row, col, num)
    )

    def fill_box(self, row_start, col_start):
        number_bank = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                num = random.choice(number_bank)
                self.board[i][j] = num
                number_bank.remove(num)

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][int(col)] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][int(col)] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self) -> None:
        for i in range(self.removed_cells):
            while True:
                rand_row = random.randint(0, int(self.row_length) - 1)
                rand_col = random.randint(0, int(self.row_length) - 1)
                if self.get_board()[rand_row][rand_col] != 0:
                    self.board[rand_row][rand_col] = 0
                    break


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
