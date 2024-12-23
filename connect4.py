def get_user_input(board):
    maxl = len(board)
    while True:
        ui = input("Select a column: ")
        try:
            tmp = int(ui)
            if tmp > 0 and tmp <= maxl + 1:

                if board[0][tmp - 1] == 0:
                    return tmp - 1
                else:
                    print("please select a column with space")
            else:
                print("please input a number between 1 and 7")
        except:
            print("please input a number :(")


def check_win(board, col):
    for r in range(0, len(board)):
        if board[r][col] != 0:
            for i in range(-3, 4):
                res = check_left(board, r, col + i)
                if res != 0:
                    # print(r, col + i, " left")
                    return res
                res = check_right(board, r, col + i)
                if res != 0:
                    # print(r, col + i, " right")
                    return res
            res = check_down(board, r, col)
            if res != 0:
                # print("down")
                return res
            return check_diagnol(board, r, col)
    return 0


def check_left(board, r, c):
    if c < 3 or c >= len(board[r]):
        return 0
    for i in range(1, 4):
        if board[r][c] != board[r][c - i]:
            return 0
    return board[r][c]


def check_right(board, r, c):
    if c > 3 or c < 0:
        return 0
    for i in range(1, 4):
        if board[r][c] != board[r][c + i]:
            return 0
    return board[r][c]


def check_down(board, r, c):
    if r > 2:
        return 0
    for i in range(1, 4):
        if board[r][c] != board[r + i][c]:
            return 0
    return board[r][c]


def check_diagnol(board, r, c):
    for i in range(0, 4):
        res = check_up_left(board, r + i, c + i)
        if res != 0:
            # print("up left", r + i, c + i)
            return res
        res = check_up_right(board, r + i, c - i)
        if res != 0:
            # print("up right", r + i, c - i)
            return res
        res = check_down_right(board, r - i, c - i)
        if res != 0:
            # print("down right", r - i, c - i)
            return res
        res = check_down_left(board, r - i, c + i)
        if res != 0:
            # print("down left", r - i, c + i)
            return res
    return 0


def check_up_left(board, r, c):
    if r < 3 or c < 3 or r >= len(board) or c >= len(board[r]):
        return 0
    for i in range(1, 4):
        if board[r][c] != board[r - i][c - i]:
            return 0
    return board[r][c]


def check_up_right(board, r, c):
    if r < 3 or c > 3 or r >= len(board) or c < 0:
        return 0
    for i in range(1, 4):
        if board[r][c] != board[r - i][c + i]:
            return 0
    return board[r][c]


def check_down_left(board, r, c):
    if r > 2 or c < 3 or r < 0 or c >= len(board[r]):
        return 0
    for i in range(1, 4):
        if board[r][c] != board[r + i][c - i]:
            return 0
    return board[r][c]


def check_down_right(board, r, c):
    if r > 2 or c > 3 or r < 0 or c < len(board[r]):
        return 0
    for i in range(1, 4):
        if board[r][c] != board[r + i][c + i]:
            return 0
    return board[r][c]


def insert(board, col, move):
    for i in range(len(board) - 1, 0, -1):
        if board[i][col] == 0:
            board[i][col] = (move % 2) + 1
            return board
    return board


def print_board(board):
    print()
    for i in range(0, len(board)):
        print("|" + "|".join(map(convert, board[i])) + "|")
    print()
    return


def convert(t):
    if t == 2:
        return "o"
    if t == 1:
        return "x"
    return " "


def play():
    board = [[0] * 7 for _ in range(6)]
    move = 1
    result = 0
    print_board(board)
    while result == 0:
        col = get_user_input(board)
        insert(board, col, move)
        print_board(board)
        result = check_win(board, col)
        move += 1
    print("Winner is: " + convert(result))


play()
