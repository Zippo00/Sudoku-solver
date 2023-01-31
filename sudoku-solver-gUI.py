import time
import pygame 
import random
pygame.init()


boards = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ], [
        [0, 6, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 6, 5, 1, 0, 0, 0],
        [1, 0, 7, 0, 0, 0, 6, 0, 2],
        [6, 2, 0, 3, 0, 5, 0, 9, 4],
        [0, 0, 3, 0, 0, 0, 2, 0, 0],
        [4, 8, 0, 9, 0, 7, 0, 3, 6],
        [9, 0, 6, 0, 0, 0, 4, 0, 8],
        [0, 0, 0, 7, 9, 4, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 7, 0]
    ], [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], [
        [4, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 4, 2, 8, 1, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 3, 0, 7, 0, 5, 4, 6, 9],
        [0, 0, 9, 3, 6, 0, 0, 8, 7],
        [0, 0, 0, 2, 8, 3, 0, 0, 0],
        [0, 0, 0, 2, 8, 3, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [2, 0, 4, 0, 1, 9, 5, 0, 0]
    ], [
        [0, 1, 0, 3, 0, 0, 0, 0, 0],
        [7, 5, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 3, 8],
        [9, 6, 2, 4, 1, 0, 8, 0, 3],
        [0, 0, 0, 7, 6, 0, 0, 0, 4],
        [0, 7, 4, 0, 0, 0, 1, 0, 6],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 3, 1, 6, 0, 2, 0, 8, 0],
        [0, 4, 9, 0, 3, 0, 0, 0, 0]
    ], [
        [0, 0, 0, 0, 2, 0, 0, 7, 4],
        [0, 0, 0, 0, 0, 0, 1, 8, 0],
        [0, 3, 7, 4, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [5, 0, 4, 0, 0, 6, 0, 0, 0],
        [6, 1, 0, 2, 0, 0, 7, 0, 3],
        [0, 6, 1, 0, 0, 9, 8, 2, 7],
        [4, 9, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0]
    ]


class Grid:
    '''
    '''
    

    def __init__(self, rows, cols, width, height, win):
        
        self.board = boards[random.randint(0,5)]
        print(boards[0])
        print(self.board)
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.update_model()
        self.selected = None, None
        self.win = win


    def update_model(self):
        '''
        '''
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def update_to_original(self):
        '''
        '''
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height) for j in range(self.cols)] for i in range(self.rows)]

    def place(self, value):
        '''
        '''
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            #self.cubes[row][col].value = value
            #self.update_model()
            if valid_move(self.model, value, (row,col)):
                self.cubes[row][col].value = value
                self.update_model()
                if self.solve():
                    return True
            self.cubes[row][col].value = 0
            self.cubes[row][col].temp = 0
            self.update_model()
            return False

    def sketch(self, value):
        '''
        '''
        row, col = self.selected
        self.cubes[row][col].temp = value

    def draw(self):
        '''
        '''
        # Draw the grid
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.win, (0,0,0), (0, i * gap), (self.width, i * gap), thickness)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.width), thickness)

        # Draw regions
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw_cube(self.win)

    def select(self, row, col):
        '''
        '''
        # Reset others
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False
        # Selected tile
        self.cubes[row][col].selected = True
        self.selected = (row,col)

    def clear(self):
        '''
        '''
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].temp = 0

    def click(self, position):
        '''
        :return: (row, col)
        '''
        if position[0] < self.width and position[1] < self.height:
            gap = self.width / 9
            x = position[0] // gap
            y = position[1] // gap
            return(int(y),int(x))
        else:
            return None

    def finished(self):
        '''
        '''
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    def solve(self):
        '''
        '''
        empty = find_empty(self.model)
        if not empty:
            return True
        row, col = empty
        for i in range(1, 10):
            if valid_move(self.model, i, (row,col)):
                self.model[row][col] = i
                if self.solve():
                    return True
                self.model[row][col] = 0
        return False

    def graphic_solve(self):
        '''
        '''
        self.update_model()
        empty = find_empty(self.model)
        if not empty:
            return True
        row, col = empty

        for i in range(1, 10):
            if valid_move(self.model, i, (row,col)):
                self.model[row][col] = i
                self.cubes[row][col].value = i
                self.cubes[row][col].draw_change(self.win, True)
                self.update_model()
                pygame.display.update()
                pygame.time.delay(100)

                if self.graphic_solve():
                    return True
                self.model[row][col] = 0
                self.cubes[row][col].value = 0
                self.update_model()
                self.cubes[row][col].draw_change(self.win, False)
                pygame.display.update()
                pygame.time.delay(100)
        return False   




class Cube:
    '''
    '''
    rows = 9 
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw_cube(self, win):
        '''
        '''
        font = pygame.font.SysFont("roboto", 40)
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif self.value != 0:
            text = font.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def draw_change(self, win, g=True):
        '''
        '''
        font = pygame.font.SysFont("roboto", 40)
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)
        text = font.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)




def valid_move(board, value, pos):
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

def window_redraw(win, board, time, mousepos, wrong=False):
    '''
    Draw the window that user sees
    '''
    win.fill((255, 255, 255))
    # Draw Time
    font = pygame.font.SysFont("roboto", 30)
    text = font.render("Time: " + time_format(time), 1, (0, 0, 0))
    win.blit(text, (540 - 140, 560))

    # Draw indication for wrong answer
    if wrong:
        text = font.render("Wrong", 1, (255, 0, 0))
    else:
        text = font.render("", 1, (255, 0, 0))
    win.blit(text, (20, 560))

    # Draw grid + board
    board.draw()
    for i in range(len(board.cubes)):
        for j in range(len(board.cubes[0])):
            board.cubes[i][j].draw_cube
    
    # Draw NewGame-button   
    text = font.render("New Game", 1, (0, 0, 0))
    if 200 <= mousepos[0] <= 325 and 553 <= mousepos[1] < 586:
        pygame.draw.rect(win,(190,190,190),(200,553,125,33))
    else:
        pygame.draw.rect(win,(220,220,220),(200,553,125,33))
    win.blit(text, (210, 560))

def time_format(seconds):
    '''
    '''
    second = seconds % 60
    minute = seconds // 60
    if minute < 10:
        if second < 10:
            formated = " 0" + str(minute) + ":0" + str(second)
        else:
            formated = " " + str(minute) + ":" + str(second)
    else:
        if second < 10:
            formated = " 0" + str(minute) + ":0" + str(second)
        else:
            formated = " " + str(minute) + ":" + str(second)
    return formated

def main():
    window = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku Puzzles")
    board = Grid(9, 9, 540, 540, window)
    key = None
    wrong = False
    game_finished = False
    startTime = time.time()
    while True:
        play_time = round(time.time() - startTime)
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == 51:
                    key = 3
                if event.key == 52:
                    key = 4
                if event.key == 53:
                    key = 5
                if event.key == 54:
                    key = 6
                if event.key == 55:
                    key = 7
                if event.key == 56:
                    key = 8
                if event.key == 57:
                    key = 9
                if event.key == 1073741913:
                    key = 1
                if event.key == 1073741914:
                    key = 2
                if event.key == 1073741915:
                    key = 3
                if event.key == 1073741916:
                    key = 4
                if event.key == 1073741917:
                    key = 5
                if event.key == 1073741918:
                    key = 6
                if event.key == 1073741919:
                    key = 7
                if event.key == 1073741920:
                    key = 8
                if event.key == 1073741921:
                    key = 9
                if event.key == pygame.K_SPACE:
                    game_finished = True
                    time_finished = play_time
                    board.update_to_original()
                    board.graphic_solve()
                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                    key = None
                if event.key == 127:
                    board.clear()
                    key = None
                if event.key == 13:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                            wrong = False
                        else:
                            print("Wrong")
                            wrong = True
                        key = None
                        if board.finished():
                            print("Game Over")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                click = board.click(mouse_position)
                if click:
                    board.select(click[0], click[1])
                    key = None
                if 200 <= mouse_position[0] <= 325 and 553 <= mouse_position[1] < 586:
                    main()
        if board.selected and key is not None:
            board.sketch(key)
        if wrong:
            window_redraw(window, board, play_time, mouse_position, wrong=True)
        else:
            if game_finished:
                window_redraw(window, board, time_finished, mouse_position)
            else:
                window_redraw(window, board, play_time, mouse_position)
        pygame.display.update()



main()
