import random


class SudokuPuzzle:

    def __init__(self, size, difficulty):
        self._size = size
        self._difficulty = difficulty.lower()
        if size == 4 and self._difficulty == 'e':
            self._board = random.choice(easy_four_boards)
        elif size == 4 and self._difficulty == 'h':
            self._board = random.choice(difficult_four_boards)
        elif size == 9 and self._difficulty == 'e':
            self._board = random.choice(easy_nine_boards)
        else:
            self._board = random.choice(difficult_nine_boards)

    def get_board(self):
        return self._board


# Easy 9x9 boards
easy_nine_boards = [
    [
        # 8989
        [0, 0, 4, 3, 6, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 5, 0, 7],
        [0, 0, 9, 8, 0, 0, 0, 0, 3],
        [0, 0, 8, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 8, 0, 1, 0, 0],
        [9, 0, 0, 0, 0, 4, 8, 0, 0],
        [5, 0, 6, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 1, 9, 7, 0, 0]
    ],
    [
        # 5275
        [9, 0, 0, 0, 0, 6, 0, 4, 0],
        [0, 0, 0, 7, 3, 0, 8, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 7, 1],
        [0, 0, 9, 0, 0, 0, 0, 8, 0],
        [6, 0, 0, 3, 0, 1, 0, 0, 7],
        [0, 4, 0, 0, 0, 0, 3, 0, 0],
        [2, 7, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 8, 0, 6, 2, 0, 0, 0],
        [0, 1, 0, 9, 0, 0, 0, 0, 4]
    ],
    [
        # 1787
        [0, 6, 0, 8, 0, 0, 0, 9, 0],
        [5, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 2, 6, 0, 1],
        [0, 0, 2, 0, 3, 4, 0, 5, 8],
        [0, 4, 7, 0, 0, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 5, 0, 3, 0, 6, 0, 0, 0],
        [0, 8, 0, 4, 1, 0, 0, 0, 0]

    ]

]

difficult_nine_boards = [
    [
        # 1
        [0, 0, 4, 0, 0, 0, 3, 0, 0],
        [2, 0, 0, 7, 0, 9, 0, 0, 8],
        [0, 6, 0, 5, 0, 4, 0, 7, 0],
        [0, 0, 5, 0, 7, 0, 2, 0, 0],
        [4, 0, 0, 3, 0, 5, 0, 0, 9],
        [0, 0, 7, 0, 9, 0, 5, 0, 0],
        [0, 4, 0, 9, 0, 2, 0, 5, 0],
        [8, 0, 0, 6, 0, 7, 0, 0, 2],
        [0, 0, 9, 0, 0, 0, 1, 0, 0]
    ],
    [   # 2
        [1, 5, 0, 3, 0, 6, 0, 8, 9],
        [4, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 4, 2, 8, 0, 0, 0],
        [9, 0, 5, 0, 3, 0, 8, 0, 6],
        [0, 0, 3, 1, 0, 9, 7, 0, 0],
        [2, 0, 6, 0, 5, 0, 3, 0, 1],
        [0, 0, 0, 2, 1, 3, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 3],
        [3, 9, 0, 6, 0, 7, 0, 5, 8]

    ],
    [
        # 3
        [9, 8, 0, 1, 0, 7, 0, 6, 2],
        [4, 0, 0, 8, 0, 6, 0, 0, 3],
        [0, 0, 7, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [8, 0, 4, 0, 0, 0, 5, 0, 1],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 3, 0, 0],
        [7, 0, 0, 6, 0, 3, 0, 0, 4],
        [3, 5, 0, 9, 0, 4, 0, 1, 6]
    ]

]

# 4x4 Puzzles generated from sudoku-download.net
# Easy 4x4 boards
easy_four_boards = [
    # 3
    [
        [4, 2, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 2, 0],
        [0, 0, 0, 3]
    ],
    [
        # 5
        [0, 2, 0, 0],
        [0, 0, 2, 0],
        [3, 0, 4, 0],
        [2, 0, 0, 1]
    ],
    [
        # 13
        [4, 0, 2, 1],
        [0, 0, 0, 3],
        [0, 0, 0, 0],
        [0, 2, 3, 0]
    ],
    [
        # 2
        [1, 0, 3, 4],
        [0, 3, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 1]
    ]
]

# Difficult 4x4 boards
difficult_four_boards = [
    # 1
    [
        [3, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, 0]
    ],
    # 2
    [
        [4, 0, 0, 0],
        [0, 0, 4, 0],
        [0, 0, 0, 3],
        [0, 2, 0, 0]
    ],
    # 7
    [
        [0, 0, 1, 0],
        [0, 4, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 1]
    ],
    # 8
    [
        [0, 0, 0, 3],
        [0, 3, 0, 0],
        [4, 0, 0, 0],
        [0, 0, 1, 0]
    ]
]
