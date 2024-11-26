WHITE_KING = ("♔", "k")
WHITE_QUEEN = ("♕", "q")
WHITE_ROOK = ("♖", "r")
WHITE_BISHOP = ("♗", "b")
WHITE_KNIGHT = ("♘", "n")
WHITE_PAWN = ("♙", "p")

BLACK_KING = ("♚", "K")
BLACK_QUEEN = ("♛", "Q")
BLACK_ROOK = ("♜", "R")
BLACK_BISHOP = ("♝", "B")
BLACK_KNIGHT = ("♞", "N")
BLACK_PAWN = ("♟", "P")

BLACK_FIGURES = BLACK_KING + BLACK_QUEEN + BLACK_ROOK + BLACK_BISHOP + BLACK_KNIGHT + BLACK_PAWN
WHITE_FIGURES = WHITE_KING + WHITE_QUEEN + WHITE_ROOK + WHITE_BISHOP + WHITE_KNIGHT + WHITE_PAWN
ALL_FIGURES = BLACK_FIGURES + WHITE_FIGURES


def white_pawn(i, j, white, board):
    """
    i- = up
    j+ = right
    j- = left
    """
    white[i][j] = board[i][j]
    if i > 0:
        if j > 0 and j < 7:
            if board[i-1][j] not in BLACK_FIGURES:
                white[i - 1][j] = board[i - 1][j]
            white[i - 1][j + 1] = board[i - 1][j + 1]
            white[i - 1][j - 1] = board[i - 1][j - 1]
        if j == 0:
            if board[i-1][j] not in BLACK_FIGURES:
                white[i - 1][j] = board[i - 1][j]
            white[i - 1][j + 1] = board[i - 1][j + 1]
        if j == 7:
            if board[i-1][j] not in BLACK_FIGURES:
                white[i - 1][j] = board[i - 1][j]
            white[i - 1][j - 1] = board[i - 1][j - 1]

def black_pawn(i, j, black, board):
    """ 
    i+ = down
    j+ = right
    j- = left
    """
    black[i][j] = board[i][j]
    if i < 7:
        if j > 0 and j < 7:
            if board[i+1][j] not in WHITE_FIGURES:
                black[i + 1][j] = board[i + 1][j]
            black[i + 1][j + 1] = board[i + 1][j + 1]
            black[i + 1][j - 1] = board[i + 1][j - 1]
        if j == 0:
            if board[i+1][j] not in WHITE_FIGURES:
                black[i + 1][j] = board[i + 1][j]
            black[i + 1][j + 1] = board[i + 1][j + 1]
        if j == 7:
            if board[i+1][j] not in WHITE_FIGURES:
                black[i + 1][j] = board[i + 1][j]
            black[i + 1][j - 1] = board[i + 1][j - 1]

def king(i, j, board_color, board, color : str, black=None, white=None):
    """ 
    i+1 = down
    i-1 = up
    j+1 = right
    j-1 = left
    """
    board_color[i][j] = board[i][j]
    if i > 0 and i < 7: # if king is not on the edge of the board
        if j > 0 and j < 7: # if king is not on the edge of the board
            board_color[i + 1][j] = board[i + 1][j]
            board_color[i + 1][j + 1] = board[i + 1][j + 1]
            board_color[i + 1][j - 1] = board[i + 1][j - 1]
            board_color[i][j + 1] = board[i][j + 1]
            board_color[i][j - 1] = board[i][j - 1]
            board_color[i - 1][j] = board[i - 1][j]
            board_color[i - 1][j + 1] = board[i - 1][j + 1]
            board_color[i - 1][j - 1] = board[i - 1][j - 1]
        if j == 0: # if king is on the left edge of the board
            board_color[i + 1][j] = board[i + 1][j]
            board_color[i + 1][j + 1] = board[i + 1][j + 1]
            board_color[i][j + 1] = board[i][j + 1]
            board_color[i - 1][j] = board[i - 1][j]
            board_color[i - 1][j + 1] = board[i - 1][j + 1]
        if j == 7: # if king is on the right edge of the board
            board_color[i + 1][j] = board[i + 1][j]
            board_color[i + 1][j - 1] = board[i + 1][j - 1]
            board_color[i][j - 1] = board[i][j - 1]
            board_color[i - 1][j] = board[i - 1][j]
            board_color[i - 1][j - 1] = board[i - 1][j - 1]
    if i == 0: # if king is on the top edge of the board
        if j == 0: # if king is on the top left corner of the board
            board_color[i + 1][j] = board[i + 1][j]
            board_color[i + 1][j + 1] = board[i + 1][j + 1]
            board_color[i][j + 1] = board[i][j + 1]
        if j == 7: # if king is on the top right corner of the board
            board_color[i + 1][j] = board[i + 1][j]
            board_color[i + 1][j - 1] = board[i + 1][j - 1]
            board_color[i][j - 1] = board[i][j - 1]
        if j > 0 and j < 7: # if king is on the top edge of the board but not on the corners
            board_color[i + 1][j] = board[i + 1][j]
            board_color[i + 1][j + 1] = board[i + 1][j + 1]
            board_color[i + 1][j - 1] = board[i + 1][j - 1]
            board_color[i][j + 1] = board[i][j + 1]
            board_color[i][j - 1] = board[i][j - 1]
    if i == 7: # if king is on the bottom edge of the board
        if j == 0: # if king is on the bottom left corner of the board
            board_color[i - 1][j] = board[i - 1][j]
            board_color[i - 1][j + 1] = board[i - 1][j + 1]
            board_color[i][j + 1] = board[i][j + 1]
        if j == 7: # if king is on the bottom right corner of the board
            board_color[i - 1][j] = board[i - 1][j]
            board_color[i - 1][j - 1] = board[i - 1][j - 1]
            board_color[i][j - 1] = board[i][j - 1]
        if j > 0 and j < 7: # if king is on the bottom edge of the board but not on the corners
            board_color[i - 1][j] = board[i - 1][j]
            board_color[i - 1][j + 1] = board[i - 1][j + 1]
            board_color[i - 1][j - 1] = board[i - 1][j - 1]
            board_color[i][j + 1] = board[i][j + 1]
            board_color[i][j - 1] = board[i][j - 1]
    
    if color == 'black':
        black = board_color
    if color == 'white':
        white = board_color

def rook(i, j, board_color, board, color : str, black=None, white=None):
    """
    m+ = down
    m- = up
    n+ = right
    n- = left
    """
    board_color[i][j] = board[i][j]
    m, n = i,j
    while n < 7: # while not on the right edge of the board
        board_color[m][n + 1] = board[m][n + 1]
        if board[m][n + 1] in ALL_FIGURES: # if there is a figure on the way, stop
            break
        n += 1
    m, n = i, j
    while n > 0: # while not on the left edge of the board
        board_color[m][n - 1] = board[m][n - 1]
        if board[m][n - 1] in ALL_FIGURES:
            break
        n -= 1
    m, n = i, j
    while m < 7: # while not on the bottom edge of the board
        board_color[m + 1][n] = board[m + 1][n]
        if board[m + 1][n] in ALL_FIGURES:
            break
        m += 1
    m, n = i, j
    while m > 0: # while not on the top edge of the board
        board_color[m - 1][n] = board[m - 1][n]
        if board[m - 1][n] in ALL_FIGURES:
            break
        m -= 1
    
    if color == 'black':
        black = board_color
    else:
        white = board_color
        
def bishop(i, j, board_color, board, color : str, black=None, white=None):
    """
    m+ = down
    m- = up
    n+ = right
    n- = left
    """
    board_color[i][j] = board[i][j]
    m, n = i, j
    while m < 7 and n < 7: # while not on the bottom right corner of the board
        board_color[m + 1][n + 1] = board[m + 1][n + 1]
        if board[m + 1][n + 1] in ALL_FIGURES: # if there is a figure on the way, stop
            break
        m += 1
        n += 1
    m, n = i, j
    while m < 7 and n > 0: # while not on the bottom left corner of the board
        board_color[m + 1][n - 1] = board[m + 1][n - 1]
        if board[m + 1][n - 1] in ALL_FIGURES:
            break
        m += 1
        n -= 1
    m, n = i, j
    while m > 0 and n < 7: # while not on the top right corner of the board
        board_color[m - 1][n + 1] = board[m - 1][n + 1]
        if board[m - 1][n + 1] in ALL_FIGURES:
            break
        m -= 1
        n += 1
    m, n = i, j
    while m > 0 and n > 0: # while not on the top left corner of the board
        board_color[m - 1][n - 1] = board[m - 1][n - 1]
        if board[m - 1][n - 1] in ALL_FIGURES: 
            break
        m -= 1
        n -= 1
    
    if color == 'black':
        black = board_color
    else:
        white = board_color
        
def queen(i, j, board_color, board, color : str, black=None, white=None):
    rook(i, j, board_color, board, color, black=black, white=white)
    bishop(i, j, board_color, board, color, black=black, white=white)
    
def knight(i, j, board_color, board, color : str, black=None, white=None):
    """ 
    i+ = down
    i- = up
    j+ = right
    j- = left 
    """
    board_color[i][j] = board[i][j]
    if i > 0 and j > 1: 
        board_color[i - 1][j - 2] = board[i - 1][j - 2]
    if i > 0 and j < 6: 
        board_color[i - 1][j + 2] = board[i - 1][j + 2]
    if i > 1 and j > 0: 
        board_color[i - 2][j - 1] = board[i - 2][j - 1]
    if i > 1 and j < 7: 
        board_color[i - 2][j + 1] = board[i - 2][j + 1]
    if i < 7 and j > 1:
        board_color[i + 1][j - 2] = board[i + 1][j - 2]
    if i < 7 and j < 6:
        board_color[i + 1][j + 2] = board[i + 1][j + 2]
    if i < 6 and j > 0:
        board_color[i + 2][j - 1] = board[i + 2][j - 1]
    if i < 6 and j < 7: 
        board_color[i + 2][j + 1] = board[i + 2][j + 1]
        
    if color == 'black':
        black = board_color
    else:
        white = board_color
        
def calculate_coverage (board):
    board2 = ['?' * 8 for _ in range(8)] # 8x8 board with all cells as '?'
    white = [list(row) for row in board2] 
    black = [list(row) for row in board2]
    
    for i in range(8):
        for j in range(8):
            if board[i][j] in BLACK_ROOK:
                rook(i, j, black, board, 'black', black=black)
            if board[i][j] in BLACK_KNIGHT:
                knight(i, j, black, board, 'black', black=black)
                
            if board[i][j] in BLACK_BISHOP:
                bishop(i, j, black, board, 'black', black=black)
                    
            if board[i][j] in BLACK_KING:
                king(i, j, black, board, 'black', black=black)
                    
            if board[i][j] in BLACK_QUEEN:
                queen(i, j, black, board, 'black', black=black)
            
            if board[i][j] in BLACK_PAWN:
                black_pawn(i, j, black, board)
            
            if board[i][j] in WHITE_PAWN:
                white_pawn(i, j, white, board)
            
            if board[i][j] in WHITE_ROOK:
                rook(i, j, white, board, 'white', white=white)
                
            if board[i][j] in WHITE_KNIGHT:
                knight(i, j, white, board, 'white', white=white)
            
            if board[i][j] in WHITE_BISHOP:
                bishop(i, j, white, board, 'white', white=white)
            
            if board[i][j] in WHITE_KING:
                king(i, j, white, board, 'white', white=white)
            
            if board[i][j] in WHITE_QUEEN:
                queen(i, j, white, board, 'white', white=white)

    white = [''.join(row) for row in white] # convert list of lists to list of strings
    black = [''.join(row) for row in black]
    
    return white, black

def print_normal_board(board, color='Both'):
    print(f"{color} side board coverage:\n")
    for line in board:
        print(str(line))
    print("---------------------")
    
def print_prettified_board(board, color='Both'):
    list_board = [list(row) for row in board]
    
    print(f"{color} side board coverage (prettified):\n")
    print("   A     B     C     D     E     F     G     H")
    
    print("------" * 8)
    for i in range(8):
        print("|", end="")
        print("     |" * 8)
        print("|", end="")
        for j in range(8):
            print("  " + list_board[i][j] + "  |", end="")
        print(" ", str(i + 1))
        print("|", end="")
        print("     |" * 8)
        print("------" * 8)
        
    print("\n","-"*100,"\n\n")

def main():
   
    chess_board = [
        "♜♞♝♛♚♝♞♜",
        "♟♟♟♟♟♟♟♟",
        "........",
        "........",
        "........",
        "........",
        "♙♙♙♙♙♙♙♙",
        "♖♘♗♕♔♗♘♖",
    ]
    
    # chess_board = [
    #     "....p...",
    #     "........",
    #     "R.....Q.",
    #     "p.......",
    #     "........",
    #     "........",
    #     "....K...",
    #     "........",
    # ]
    
    white, black = calculate_coverage(chess_board)
    print_normal_board(board=chess_board)
    print_normal_board(white, color='White')
    print_normal_board(black, color='Black')
    
    print("\n\n\n\n")
    
    print_prettified_board(board=chess_board)
    print_prettified_board(white, color='White')
    print_prettified_board(black, color='Black')

if __name__ == "__main__":
    main()
 