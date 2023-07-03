from abc import ABC, abstractmethod


class SudokuSolver(ABC):
    def __init__(self, board):
        self.board = board
        self.steps = 0

    def is_complete(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        return True

    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return -1, -1

    def is_valid(self, row, col, num):
        # Verificar en la fila
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Verificar en la columna
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Verificar en el cuadro 3x3
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True
    
    @abstractmethod
    def solve_sudoku(self):
        pass


class BacktrackingSolver(SudokuSolver):
    def solve_sudoku(self):
        if self.is_complete():
            return True

        row, col = self.find_empty_cell()

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve_sudoku():
                    return True

                self.board[row][col] = 0
                self.steps += 1

        return False


class ForwardCheckingSolver(SudokuSolver):
    def solve_sudoku(self):
        if self.is_complete():
            return True

        row, col = self.find_empty_cell()
        domain = self.get_domain(row, col)

        for num in domain:
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.forward_checking(row, col) and self.solve_sudoku():
                    return True

                self.board[row][col] = 0
                self.steps += 1

        return False


    def forward_checking(self, row, col):
        for i in range(9):
            if self.board[row][i] == 0:
                if not self.has_valid_domain(row, i):
                    return False

        for i in range(9):
            if self.board[i][col] == 0:
                if not self.has_valid_domain(i, col):
                    return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == 0:
                    if not self.has_valid_domain(start_row + i, start_col + j):
                        return False

        return True


    def has_valid_domain(self, row, col):
        domain = self.get_domain(row, col)
        return len(domain) > 0


    def get_domain(self, row, col):
        domain = set(range(1, 10))

        for i in range(9):
            domain.discard(self.board[row][i])
            domain.discard(self.board[i][col])

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                domain.discard(self.board[start_row + i][start_col + j])

        return domain