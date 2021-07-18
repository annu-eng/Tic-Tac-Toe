board = ["-", "-", "-",
         "-", "-", "-",  # Design the board
         "-", "-", "-"]
game_still_going = True
global winner
current_player=input('who would like to play first X or O ?')
current_player = current_player.upper()
while current_player not in ["X", "O"]:
    current_player = input('who would like to play first X or O ?')
    current_player = current_player.upper()

def check_rows():x
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[1]
    elif row_2:
        return board[3]
    elif row_3:
        return board[4]
    return


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = "O"
    elif current_player == 'O':
        current_player = 'X'
    return


def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[4]
    elif column_3:
        return board[5]
    return


def check_diagnols():
    global game_still_going
    diagnol_1 = board[0] == board[4] == board[8] != '-'
    diagnol_2 = board[2] == board[4] == board[6] != '-'
    if diagnol_1 or diagnol_2:
        game_still_going = False
    if diagnol_1:
        return board[0]
    elif diagnol_2:
        return board[2]
    return


def check_if_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagnol_winner = check_diagnols()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagnol_winner:
        winner = diagnol_winner
    else:
        winner = None
        return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def check_if_game_over():
    check_if_winner()
    check_if_tie()
    return


def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def handle_turn(player):
    print('Its ' + player + "'s turn now.")
    position = input('enter your position(1-9)')
    valid_input = False
    while not valid_input:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8","9"]:  # keep on looping until postion is not in ["....."]
            position = input("please enter a number between 1 to 10")  # once in it, get out of loop
        position = int(position) - 1
        if board[position] == '-':
            valid_input = True
        else:
            print('That position is already filled, please enter a different position')
    board[position] = player
    display_board()
    return


while game_still_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
if winner == "X" or winner == "O":
    print('congratulations! '+ winner + ", you won.")
elif winner == None:
    print('Its a tie between X and O.')
