import os
import time
from random import randint

### GLOBAL METHODS

# Clear screen
def clear():
    os.system('cls')

# Timer
def wait(seconds):
    time.sleep(seconds)

### ROUND METHODS

# Draw updated board
def draw_board(board):
    clear()
    board.display_board()

# Get valid position
def get_position(players, board, char):

    answer_not_compatible = True
    position = ""

    while answer_not_compatible:
        # Print board and ask input
        draw_board(board)
        position = input("%s turn - Enter position of %s: " % (players[char].name, char))

        # Checks if the answer is a valid position
        try:
            board.__getPosition__(position)
            
            if board.__getPosition__(position) == "X" or board.__getPosition__(position)== "O":
                raise Exception("Position already chosen.")

            answer_not_compatible = False

        except:
            print("Position not valid, choose an available number")
            wait(2)
    
    return position

# Check winners
def check_winner(board):
    """ Possible combinations:
    1 - 2 - 3 | 4 - 5 - 6 | 7 - 8 - 9
    1 - 4 - 7 | 2 - 5 - 8 | 3 - 6 - 9
    1 - 5 - 9 | 3 - 5 - 7
    """

    if (board.__getPosition__("1") == board.__getPosition__("2") == board.__getPosition__("3")) \
    or (board.__getPosition__("4") == board.__getPosition__("5") == board.__getPosition__("6")) \
    or (board.__getPosition__("7") == board.__getPosition__("8") == board.__getPosition__("9")) \
    or (board.__getPosition__("1") == board.__getPosition__("4") == board.__getPosition__("7")) \
    or (board.__getPosition__("2") == board.__getPosition__("5") == board.__getPosition__("8")) \
    or (board.__getPosition__("3") == board.__getPosition__("6") == board.__getPosition__("9")) \
    or (board.__getPosition__("1") == board.__getPosition__("5") == board.__getPosition__("9")) \
    or (board.__getPosition__("3") == board.__getPosition__("5") == board.__getPosition__("7")):
        return True
    else:
        return False
    
# Declare the winner with the updated board
def declare_winner(board, winner):
    # Print board with the victory
    draw_board(board)
    print("Yay! %s won the game!" % winner)

# Check if the board is complete and it was a tie
def check_tie(board):
    values = board.__getValues__()
    count = 0 
    for value in values:
        if value == "X" or value == "O":
            count += 1
        
    return count == 9

# Declare a tie with the updated board
def declare_tie(board):
    # Print board with the tie
    draw_board(board)
    print("Round has ended. It was a tie!")

### GAME METHODS    

# Define which char starts
def random_player():
    index = randint(1, 2)
    char = ""

    if index == 1:
        char = "X"
    else:
        char = "O"
    
    return char
