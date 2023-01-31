import pprint

'''
Solves unsolved Sudoku puzzles using recursive backtracking algorithm
'''

def solve(board):
    '''
    Solves a given sudoku board using backtracking algorithm
    :param board: 2D list of integers
    :return: The solved sudoku board
    '''
    empty = find_empty(board)
    if empty:
        row, col = empty
    else:
        return True
    for i in range(1,10):
        if valid_move(board, (row, col), i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def valid_move(board, pos, value):
    '''
    Returns True if the attempted move is valid, else False
    :param board: 2D list of integers
    :param pos: (row, col)
    :param value: int
    :return: Boolean
    '''
    regions = [
                [board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]],
                [board[0][3], board[0][4], board[0][5], board[1][3], board[1][4], board[1][5], board[2][3], board[2][4], board[2][5]],
                [board[0][6], board[0][7], board[0][8], board[1][6], board[1][7], board[1][8], board[2][6], board[2][7], board[2][8]],
                [board[3][0], board[3][1], board[3][2], board[4][0], board[4][1], board[4][2], board[5][0], board[5][1], board[5][2]],
                [board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3], board[5][4], board[5][5]],
                [board[3][6], board[3][7], board[3][8], board[4][6], board[4][7], board[4][8], board[5][6], board[5][7], board[5][8]],
                [board[6][0], board[6][1], board[6][2], board[7][0], board[7][1], board[7][2], board[8][0], board[8][1], board[8][2]],
                [board[6][3], board[6][4], board[6][5], board[7][3], board[7][4], board[7][5], board[8][3], board[8][4], board[8][5]],
                [board[6][6], board[6][7], board[6][8], board[7][6], board[7][7], board[7][8], board[8][6], board[8][7], board[8][8]]
    ]
    regionPos = [
                [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    ]

    # Check given row for validity
    for i, j in enumerate(board):
        if board[pos[0]][i] == value:
            return False
    # Check given column for validity
    for i, j in enumerate(board):
        if board[i][pos[1]] == value:
            return False
    # Check the region of given pos for validity
    for i in range(len(board)):
        if pos in regionPos[i]:
            for j in range(len(board)):
                if regions[i][j] == value:
                    return False
    return True

def find_empty(board):
    '''
    Finds an empty slot in the board and returns it
    :param board: 2D list of integers
    :return: (row, col)
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

boardExample1 = [
                [7, 8, 0, 4, 0, 0, 1, 2, 0],
                [6, 0, 0, 0, 7, 5, 0, 0, 9],
                [0, 0, 0, 6, 0, 1, 0, 7, 8],
                [0, 0, 7, 0, 4, 0, 2, 6, 0],
                [0, 0, 1, 0, 5, 0, 9, 3, 0],
                [9, 0, 4, 0, 6, 0, 0, 0, 5],
                [0, 7, 0, 3, 0, 0, 0, 1, 2],
                [1, 2, 0, 0, 0, 7, 4, 0, 0],
                [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
boardExample2 = [
                [0, 6, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 6, 5, 1, 0, 0, 0],
                [1, 0, 7, 0, 0, 0, 6, 0, 2],
                [6, 2, 0, 3, 0, 5, 0, 9, 4],
                [0, 0, 3, 0, 0, 0, 2, 0, 0],
                [4, 8, 0, 9, 0, 7, 0, 3, 6],
                [9, 0, 6, 0, 0, 0, 4, 0, 8],
                [0, 0, 0, 7, 9, 4, 0, 0, 0],
                [0, 5, 0, 0, 0, 0, 0, 7, 0]
]
boardExample3 = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


pprinter = pprint.PrettyPrinter(width=41, compact=True)
solve(boardExample2)
pprinter.pprint(boardExample2)
