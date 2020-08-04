from math import sqrt as sqrt
import sudoku_puzzles as sp


class SudokuSolver:

    def __init__(self, board):
        self._board = board

    def print_board(self):
        """Prints the board in a readable format."""
        n = len(self._board)
        square = int(sqrt(len(self._board)))
        for i in range(n):
            if i % square == 0 and i != 0:
                if square == 2:
                    print('-----------')
                else:
                    print('-----------------------')
            for j in range(n):
                if (j + 1) % square == 0:
                    print(self._board[i][j], end=" | ")
                else:
                    print(self._board[i][j], end=" ")
            print("")

    def find_empty_loc(self):
        """Checks for an empty location in the board."""
        # For every row
        for y in range(len(self._board)):
            # For every column
            for x in range(len(self._board[0])):
                if self._board[y][x] == 0:
                    # Return a tuple in row, column format with an empty square
                    return y, x
        return None

    def is_possible(self, y, x, num):
        """Helper function that checks if the move to the desired square is possible.
        Args:
            board, row, column, digit to be placed in square.

        Returns True or False."""
        # Check row
        for i in range(len(self._board[y])):
            if self._board[y][i] == num:
                return False
        # Check column
        for i in range(len(self._board[y])):
            if self._board[i][x] == num:
                return False

        # Check surrounding region in 3x3 square
        area_size = int(sqrt(len(self._board)))
        area_y = (y // area_size) * area_size
        area_x = (x // area_size) * area_size

        for i in range(area_size):
            for j in range(area_size):
                if self._board[area_y + i][area_x + j] == num:
                    return False

        return True

    def solve_board(self):
        if self.find_empty_loc() is not None:
            row = self.find_empty_loc()[0]
            col = self.find_empty_loc()[1]
        else:
            return True

        for i in range(1, len(self._board) + 1):
            if self.is_possible(row, col, i):
                self._board[row][col] = i
                if self.solve_board():
                    return True
                self._board[row][col] = 0

        return False


board_size = int(input("\nWhich board size would you like to use, 4x4 or 9x9? \n(Enter 4 or 9): "))
difficulty = input("\nWhich difficulty level would you like? \nEnter E for easy or H for hard: ")

user_board = sp.SudokuPuzzle(board_size, difficulty)
solved_user_board = SudokuSolver(user_board.get_board())

print("\nYour Sudoku board prior to solving: ")
solved_user_board.print_board()
solved_user_board.solve_board()
print("\nYour Sudoku board solved: ")
solved_user_board.print_board()

