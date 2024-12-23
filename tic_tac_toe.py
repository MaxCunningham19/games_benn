dividor = "-" * 9

start_board = [[" "," "," "],[" "," "," "],[" "," "," "]]

def print_board(board):
    return "\n" + print_board_row(board[0]) + "\n" + dividor + "\n" + print_board_row(board[1]) + "\n"  + dividor + "\n" + print_board_row(board[2]) + "\n"
    
def print_board_row(row):
    return " | ".join(row)


def insert(board, column, row, move):
    input_val = "o"
    if move % 2 == 1:
        input_val =  "x"
    if board[row][column] == " ":
        board[row][column] = input_val
    return board

def check_win(board):
    result = check_win_rows(board)
    if result != "":
        return result
    
    result = check_win_columns(board)
    if result != "":
        return result
    
    return check_win_diagnol(board)


def check_win_row(board, row):
    if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ":
        return board[row][0]
    return ""
    
def check_win_rows(board):
    for row in range(0,2):
        res = check_win_row(board, row)
        if res != "":
            return res
    return ""
        
def check_win_column(board, column):
    if board[0][column] == board[1][column] and board[1][column] == board[2][column] and board[2][column] != " ":
        return board[0][column]
    return ""
    
def check_win_columns(board):
    for column in range(0,2):
        res = check_win_column(board, column)
        if res != "":
            return res
    return ""
              
def check_win_diagnol(board):
    if ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[2][0] == board[1][1] and board[1][1] == board[0][2])) and board[1][1] != " ":
        return board[1][1]
    return ""
        

def play():
    while True:
        result = ""
        move = 1
        board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        while result == "":
            print(print_board(board))
            column = int(input("column: "))
            row =  int(input("row: "))
            board = insert(board,column,row,move)
            result = check_win(board)
            move += 1
        print("Winner is: " + result)
        again = input("Would you like to play again? [y/N]: ")
        if again != "y":
            return

play()