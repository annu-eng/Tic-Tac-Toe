board = ["-", "-", "-",
         "-", "-", "-",  # Design the board using a list
         "-", "-", "-"]



def display_board():                             #To print the board in 2D fromat
    
    print(board[0] + '|' + board[1] + '|' + board[2])

    print(board[3] + '|' + board[4] + '|' + board[5])

    print(board[6] + '|' + board[7] + '|' + board[8])

    return

 



            

def check_rows():     #checking for each row whether all elements are equal 
                      #at the same time they should not be equal to the space.

    row_1 = board[0] == board[1] == board[2] != '-'

    row_2 = board[3] == board[4] == board[5] != '-'

    row_3 = board[6] == board[7] == board[8] != '-'


    if row_1 or row_2 or row_3:
    
        game_still_going = False             #breaks the program from main loop

    if row_1:                    #row1 becomes =1 when all elemeents of it becomes equal to either 'x' or 'o'
                                 #which shows that winner is either 'x' or 'o'
            
        return board[0]          #any element in that row can be returned as all will be equal

    elif row_2:

        return board[3]

    elif row_3:

        return board[6]

    return                      #returns nothing if none of the row elements becomes equal.


def flip_player():
    
    global current_player              #since value of variable 'currrent_player' is going to be changed inside this function 
                                       #and is a global variable therefore its global declaration is done inside the funciton itself
    if current_player == 'X':
    
        current_player = 'O'
   
    elif current_player == 'O': 
    
        current_player = 'X'
    
    return


def check_columns():                                  #checking if there is a winner in the same way as it was done for rows
    
    global game_still_going
    
    column_1 = board[0] == board[3] == board[6] != '-'
    
    column_2 = board[1] == board[4] == board[7] != '-'
    
    column_3 = board[2] == board[5] == board[8] != '-'
    
    if column_1 or column_2 or column_3:
    
        game_still_going = False                      #breaks the program from main loop
    
    if   column_1:
    
        return board[0]
    
    elif column_2:
    
        return board[1]
    
    elif column_3:
    
        return board[2]
    
    return


def check_diagnols():                               #checking if there is a winner in the same way as it was done for rows
    
    global game_still_going
    
    diagnol_1 = board[0] == board[4] == board[8] != '-'
    
    diagnol_2 = board[2] == board[4] == board[6] != '-'
    
    if diagnol_1 or diagnol_2:
    
        game_still_going = False               #breaks the program from main loop
    
    if diagnol_1:
    
        return board[0]
    
    elif diagnol_2:
    
        return board[2]
    
    return


def check_if_winner():      #checks whether there is any winner in row or column or a diagnol by calling the concerned functions
    
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


def check_if_tie():                    #incase none of the rows or columns or diagnols has any similar elements
    
    global game_still_going
    
    if "-" not in board:
    
        game_still_going = False      #breaks the program from main loop
    
    return


def check_if_game_over():
    
    check_if_winner()
    
    check_if_tie()
    
    return



def handle_turn(player):
   
    print('Its ' + player + "'s turn now.")
   
    position = input('enter your position(1-9)')
    
    valid_input = False
    
    while not valid_input:
       
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8","9"]:  # keep on looping until postion is not in ["....."]
        
            position = input("please enter a number between 1 to 10")  # once in it, get out of loop
       
        position = int(position) - 1    # As array starts form zero
        
        if board[position] == '-':        #input is considered a valid one only if the entered postion has '-'(space) in board
          
            valid_input = True
        else:
       
            print('That position is already filled, please enter a different position')
    board[position] = player
    
    display_board()
    
    return

##########        main program          ##########

game_still_going = True             #condition based on which the program enters the main loop

current_player=input('who would like to play first X or O ?')

current_player = current_player.upper()

while current_player not in ["X", "O"]:                 #incase the user enters an undesired input

    current_player = input('who would like to play first X or O ?')

    current_player = current_player.upper()

while game_still_going:
    
    handle_turn(current_player)
    
    check_if_game_over()
    
    flip_player()


if winner == "X" or winner == "O":

    print('congratulations! '+ winner + ", you won.")

elif winner == None:

    print('Its a tie between X and O.')
